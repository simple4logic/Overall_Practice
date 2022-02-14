const range = (n) => Array.from({ length: n }).map((_, i) => i);

const delay = (n) => new Promise((r) => setTimeout(r, n));

const createGrid = (n) =>
  Array.from({ length: n }).map(() =>
    Array.from({ length: n }).map(() => 0)
  );

const draw = (container, grid) => {
  const template = grid
    .map(
      (row) =>
        `<div class="row">${row.map((i) => i.draw()).join("")}</div>`
    )
    .join("");

  container.innerHTML = template;
};

class Cell {
  constructor(x, y, size) {
    this.x = x;
    this.y = y;
    this.size = size;
    this.visited = false;
    this.walls = { left: true, right: true, top: true, bottom: true };
  }

  draw() {
    const classes = Object.entries(this.walls)
      .filter(([k, v]) => v)
      .map(([position]) => `${position}-wall`)
      .join(" ");

    const visited = this.visited ? "visited" : "";
    const size = `width: ${this.size}; height: ${this.size};`;

    return `<span style="${size}" class="cell ${classes} ${visited} "></span>`;
  }

  visit() {
    this.visited = true;
  }

  randomNeighbor(grid) {
    const { x, y } = this;
    return [
      [x - 1, y],
      [x + 1, y],
      [x, y - 1],
      [x, y + 1],
    ]
      .filter(([x, y]) => grid[y] && grid[y][x] && !grid[y][x].visited)
      .map(([x, y]) => grid[y][x])
      .sort(() => Math.random() - 0.5)[0];
  }
}

function removeWall(cell1, cell2) {
  const xDiff = cell1.x - cell2.x;
  const yDiff = cell1.y - cell2.y;

  if (xDiff === -1) {
    cell1.walls.right = false;
    cell2.walls.left = false;
  } else if (xDiff === 1) {
    cell1.walls.left = false;
    cell2.walls.right = false;
  } else if (yDiff === -1) {
    cell1.walls.bottom = false;
    cell2.walls.top = false;
  } else if (yDiff === 1) {
    cell1.walls.top = false;
    cell2.walls.bottom = false;
  }
}

const generateMaze = async (n) => {
  const size = 750 / n;

  const grid = createGrid(n).map((row, y) =>
    row.map((_, x) => new Cell(x, y, size))
  );

  const initialCell = grid[0][0];

  initialCell.visit();

  const stack = [initialCell];

  let currentCell;

  while (stack.length) {
    currentCell = stack.pop();

    const neighborCell = currentCell.randomNeighbor(grid);

    if (neighborCell) {
      stack.push(currentCell);
      removeWall(currentCell, neighborCell);
      neighborCell.visit();
      stack.push(neighborCell);
    }
  }

  const container = document.querySelector(".container");

  draw(container, grid);

  document.body.onkeydown = createNavigator(n, grid);
};

function createNavigator(n, grid) {
  const index = (x, y) => y * n + x;
  const inGrid = (x, y) => 0 <= x && x <= n && 0 <= y && y <= n;
  const point = '<div class="wrapper"><div class="point"></div></div>';

  let x = 0;
  let y = 0;
  const cells = document.querySelectorAll(".cell");
  let currentCell = cells[index(x, y)];
  let nextCell = null;
  currentCell.innerHTML = point;
  currentCell.classList.add("passed");

  cells[cells.length - 1].innerHTML = point.replace(
    "point",
    "blue point"
  );

  return (e) => {
    if (!e.key.startsWith("Arrow")) return;

    const key = e.key.slice(5).toLowerCase();

    if (key === "up") {
      if (!inGrid(x, y - 1)) return;
      if (grid[y][x].walls.top) return;
      y -= 1;
    } else if (key === "down") {
      if (!inGrid(x, y + 1)) return;
      if (grid[y][x].walls.bottom) return;
      y += 1;
    } else if (key === "left") {
      if (!inGrid(x - 1, y)) return;
      if (grid[y][x].walls.left) return;
      x -= 1;
    } else if (key === "right") {
      if (!inGrid(x + 1, y)) return;
      if (grid[y][x].walls.right) return;
      x += 1;
    }

    nextCell = cells[index(x, y)];
    nextCell.innerHTML = point;
    nextCell.classList.add("passed");

    currentCell.innerHTML = "";
    currentCell = nextCell;
  };
}

generateMaze(30);