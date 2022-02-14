/*******************functions***********************/

function randomInt(...args) {
    if (args.length === 1) {
      const [n] = args;
      return Math.ceil(Math.random() * n);
    }

    if (args.length === 2) {
      const [start, end] = args;

      if (start > end) throw Error("시작값이 끝값보다 큼");

      return Math.ceil(Math.random() * (end - start)) + start;
    }
  }

  function random(...args) {
    if (args.length === 1) {
      const [n] = args;
      return Math.random() * n;
    }

    if (args.length === 2) {
      const [start, end] = args;

      if (start > end) throw Error("시작값이 끝값보다 큼");

      return Math.random() * (end - start) + start;
    }
  }

  const range = function (n, m) {
    if (arguments.length === 1)
      return Array.from({ length: n }).map((_, i) => i);

    if (arguments.length === 2) {
      if (n === m) return [n];
      else if (n < m) {
        return Array.from({ length: m - n + 1 }).map((_, i) => i + n);
      } else {
        return Array.from({ length: n - m + 1 }).map(
          (_, i) => m - i + (n - m)
        );
      }
    }
  };

  function normalize(n) {
    return n < 0 ? -1 : n > 0 ? 1 : 0;
  }

  function clamp(v, min, max) {
    return Math.max(min, Math.min(max, v));
  }

  function between(v, min, max) {
    return min <= v && v <= max;
  }

  const delay = (n) => new Promise((r) => setTimeout(r, n));


/***************** Vector Library ******************/

 class Vector {
    constructor(x = 0, y = 0) {
      this.x = x;
      this.y = y;
    }

    add(v) {
      this.x += v.x;
      this.y += v.y;
    }

    sub(v) {
      this.x -= v.x;
      this.y -= v.y;
    }

    mult(n) {
      this.x *= n;
      this.y *= n;
    }

    mag() {
      return Math.sqrt(this.x * this.x + this.y + this.y);
    }

    get() {
      return new Vector(this.x, this.y);
    }

    normalize() {
      this.x = normalize(this.x);
      this.y = normalize(this.y);
    }

    copy() {
      return new Vector(this.x, this.y);
    }
  }

  Vector.mult = (v, n) => new Vector(v.x * n, v.y * n);

  Vector.div = (v, n) => new Vector(v.x / n, v.y / n);


/***************** Canvas Library *****************/

 const canvas = document.getElementById("canvas");
 const ctx = canvas.getContext("2d");

 const width = 710;
 const height = 880;
 const uiOffsetY = 80;

 canvas.width = width;
 canvas.height = height;

 function line(x1, y1, x2, y2, color = "#000") {
   ctx.beginPath();
   ctx.strokeStyle = color;
   ctx.lineWidth = 2;
   ctx.moveTo(x1, y1);
   ctx.lineTo(x2, y2);
   ctx.stroke();
 }

 function dashLine(x1, y1, x2, y2) {
   ctx.beginPath();
   ctx.setLineDash([5, 15]);
   ctx.moveTo(x1, y1);
   ctx.lineTo(x2, y2);
   ctx.stroke();
   ctx.setLineDash([]);
 }

 function rect(x, y, w, h) {
   ctx.beginPath();
   ctx.rect(x, y, w, h);
   ctx.strokeStyle = "#000";
   ctx.stroke();
   ctx.closePath();
 }

 function fillRect(x, y, w, h, color = "#171717") {
   ctx.save();
   ctx.beginPath();
   ctx.fillStyle = color;
   ctx.fillRect(x, y, w, h);
   ctx.stroke();
   ctx.closePath();
   ctx.restore();
 }

 function circle(x, y, r, color = "#000") {
   ctx.save();
   ctx.beginPath();
   ctx.arc(x, y, r, 0, Math.PI * 2);
   ctx.lineWidth = 3;
   ctx.fillStyle = color;
   ctx.strokeStyle = color;
   ctx.fill();
   ctx.stroke();
   ctx.closePath();
   ctx.restore();
 }

 function clear() {
   ctx.clearRect(0, 0, width, height);
 }

 function shuffle(arr) {
   return arr.sort(() => Math.random() - 0.5);
 }


 /******************** User Code ********************/
 
  const POWER = 0.3;

  const Mouse = { position: new Vector(0, 0) };

  class BallLine {
    constructor() { }

    display(state) {
      if (!state.ballMoving && !state.brickMoving && state.ballPos) {
        dashLine(
          state.ballPos.x,
          state.ballPos.y,
          Mouse.position.x,
          Math.min(Mouse.position.y, 720)
        );
      }
    }
  }

  class Ball {
    constructor(mass, x, y) {
      this.position = new Vector(x, y);
      this.velocity = new Vector(0, 0);
      this.acceleration = new Vector(0, 0);
      this.mass = mass;
      this.r = this.mass * 8;
      this.showDirection = true;
    }

    setOnStop(f) {
      this.onStop = f;
    }

    applyForce(force) {
      const f = Vector.div(force, this.mass);
      this.acceleration.add(f);
    }

    update() {
      this.velocity.add(this.acceleration);
      this.position.add(this.velocity);

      this.acceleration.mult(0);
    }

    move(direction) {
      if (direction === "right") this.applyForce(new Vector(20, 0));
      else if (direction === "left") this.applyForce(new Vector(-20, 0));
    }

    stop() {
      this.velocity = new Vector(0, 0);
      this.showDirection = true;
      this.onStop(this);
      this.downing = false;
    }

    down() {
      this.downing = true;
      this.velocity = new Vector(0, 30);
    }

    shoot(mousePos) {
      this.showDirection = false;
      const force = this.calcBallVelocity(this.angle(mousePos));
      this.applyForce(force);
    }

    calcBallVelocity(angle) {
      return new Vector(
        100 * Math.cos(angle) * POWER,
        100 * Math.sin(angle) * POWER
      );
    }

    angle(mousePos) {
      const opposite = mousePos.y - this.position.y;
      const adjacent = mousePos.x - this.position.x;
      const angle = Math.atan2(opposite, adjacent);

      return angle;
    }

    display() {
      circle(this.position.x, this.position.y, this.r, "#5ba7f4");
    }

    collideWith(brick) {
      if (this.downing) return false;

      const { x, y } = this.position;
      const r = this.r;

      const closestX = clamp(x, brick.x, brick.x + brick.w);
      const closestY = clamp(y, brick.y, brick.y + brick.h);

      const distanceX = x - closestX;
      const distanceY = y - closestY;
      const distanceSquared = distanceX * distanceX + distanceY * distanceY;

      const collided = distanceSquared < r * r;

      if (!collided) return false;

      if (
        closestY === brick.y &&
        between(closestX, brick.x - r + 3, brick.x + brick.w + r - 3)
      ) {
        this.velocity.y *= -1;
        this.position.y = closestY - r;
      } else if (
        closestY === brick.y + brick.h &&
        between(closestX, brick.x - r + 3, brick.x + brick.w + r - 3)
      ) {
        this.velocity.y *= -1;
        this.position.y = closestY + r;
      } else if (
        closestX === brick.x &&
        between(closestY, brick.y - r + 3, brick.y + brick.h + r - 3)
      ) {
        this.velocity.x *= -1;
        this.position.x = closestX - r;
      } else if (
        closestX === brick.x + brick.w &&
        between(closestY, brick.y - r + 3, brick.y + brick.h + r - 3)
      ) {
        this.velocity.x *= -1;
        this.position.x = closestX + r;
      }

      return true;
    }

    collideWithBonusBall(bonusBall) {
      if (this.downing) return false;

      const x = this.position.x - bonusBall.x;
      const y = this.position.y - bonusBall.y;
      const r = this.r;
      const collided = 2 * r >= Math.sqrt(x * x + y * y);

      return collided;
    }

    checkEdges() {
      if (this.position.x > width) {
        this.position.x = width;
        this.velocity.x *= -1;
      } else if (this.position.x < 0) {
        this.position.x = 0;
        this.velocity.x *= -1;
      }

      if (this.position.y > height - 100) {
        this.velocity.y *= -1;
        this.position.y = height - 100;
        this.stop();
      } else if (this.position.y < 100) {
        this.velocity.y *= -1;
        this.position.y = 100;
      }
    }
  }

  class Brick {
    constructor(n, x, y) {
      this.n = n;
      this.start = n;

      this.x = x * 120;
      this.y = y * 80 + uiOffsetY;
      this.w = 110;
      this.h = 70;
    }

    shouldMoveDown(state) {
      return this.y < 80 * (state.level - this.start + 1) + uiOffsetY;
    }

    update(state) {
      if (this.shouldMoveDown(state)) {
        this.y = Math.min(
          this.y + 10,
          80 * (state.level - this.start + 1) + uiOffsetY
        );
      }
    }

    color(level) {
      const percentage = ((level - this.n) / level) * 30;
      return `hsl(${percentage}, ${100 - percentage}%, 63%)`;
    }

    display(state) {
      fillRect(this.x, this.y, this.w, this.h, this.color(state.level));
      ctx.fillStyle = "black";
      ctx.font = "20px Arial";
      ctx.fillText(
        this.n,
        this.x + this.w / 2 - 8,
        this.y + this.h / 2 + 5
      );
    }

    hit() {
      this.n--;
    }

    get broken() {
      return this.n <= 0;
    }

    get hitBottom() {
      return this.y >= height - uiOffsetY - 80;
    }
  }

  class BrickParticle {
    constructor(n, x, y) {
      const i = n % 5;
      const j = ~~(n / 4);

      this.w = 22;
      this.h = 18;
      this.location = new Vector(x + i * this.w, y + j * this.h);
      this.acceleration = new Vector(0, 0);
      this.velocity = new Vector(
        i > 2
          ? random(0, 0.5)
          : i === 2
            ? random(-0.5, 0.5)
            : random(-0.5, 0),
        random(1, 3)
      );
      this.lifespan = 255;
    }

    update() {
      this.velocity.add(this.acceleration);
      this.location.add(this.velocity);
      this.lifespan -= 4;
    }

    display() {
      fillRect(
        this.location.x,
        this.location.y,
        22,
        18,
        `hsla(30, 70%, 63%, ${this.lifespan / 255})`
      );
    }

    run() {
      this.update();
      this.display();
    }

    get isDead() {
      return this.lifespan < 0;
    }
  }

  class BrickParticleSystem {
    constructor(x, y) {
      this.origin = new Vector(x, y);
      this.particles = range(20).map((n) => new BrickParticle(n, x, y));
    }

    addParticle() {
      this.particles.push(new BrickParticle(this.origin));
    }

    run() {
      this.particles.forEach((particle) => particle.run());
    }

    get isDead() {
      return !this.particles.length || this.particles[0].isDead;
    }
  }

  class BrickParticleSystems {
    constructor() {
      this.particleSystems = [];
    }

    addParticleSystem(...bricks) {
      const newPs = bricks.map(({ x, y }) => new BrickParticleSystem(x, y));
      this.particleSystems.push(...newPs);
    }

    run() {
      this.particleSystems = this.particleSystems.filter(
        (ps) => !ps.isDead
      );
      this.particleSystems.forEach((ps) => ps.run());
    }
  }

  class BonusBall {
    constructor(n, x, y) {
      this.start = n;
      this.r = 16;
      this.x = x * 120 + 56;
      this.y = y * 80 + 36 + uiOffsetY;
      this.hit = false;

      //         this.effectR = 18;
      //         this.effectD = 0.1;
    }

    moveDownLittle(state) {
      this.y = Math.min(
        this.y + 10,
        80 * (state.level - this.start + 1) + uiOffsetY + 40
      );
    }

    update(state) {
      if (this.hit) this.y = Math.min(this.y + 50, height - 100);
      else this.moveDownLittle(state);

      if (this.hit && this.y === height - 100 && state.brickMoving) {
        if (this.x < state.ballPos.x) {
          this.x = Math.min(this.x + 30, state.ballPos.x);
        } else {
          this.x = Math.max(this.x - 30, state.ballPos.x);
        }
      }

      //         this.effectR += this.effectD;
      //         if (this.effectR > 28) this.effectR = 18;
    }

    display() {
      circle(this.x, this.y, this.r, "#3dd462");
      //         if (!this.hit)
      //             circle(this.x, this.y, this.effectR);
    }

    hitWithBall() {
      this.hit = true;
    }

    collideWith(ball) {
      const x = ball.position.x - this.x;
      const y = ball.position.y - this.y;
      const r = this.r;
      const collided = 2 * r >= Math.sqrt(x * x + y * y);

      if (collided) {
        this.hit = true;
      }
      return collided;
    }
  }

  class UI {
    constructor() { }

    display(state) {
      line(0, uiOffsetY, width, uiOffsetY);
      line(0, height - uiOffsetY, width, height - uiOffsetY);

      this.showBallCount(state);
      this.showScore(state);
    }

    showScore(state) {
      ctx.fillText(`현재 점수: ${state.level}`, 30, uiOffsetY / 2 + 7);
      ctx.fillText(
        `최고 점수: ${state.bestLevel}`,
        width - 150,
        uiOffsetY / 2 + 7
      );
    }

    showBallCount(state) {
      if (!state.ballMoving)
        ctx.fillText(
          `x${state.ballCount}`,
          state.ballPos.x - 10,
          height - 55
        );
    }

    gameOver() {
      fillRect(0, height / 2 - 100, width, 200, "rgba(0, 0, 0, 0.3)");
      ctx.font = "40px Arial";
      ctx.fillText("패배!", width / 2 - 40, height / 2 + 12);
      ctx.font = "20px Arial";
    }
  }

  class Balls {
    constructor(state) {
      this.balls = range(state.ballCount).map(
        (i) => new Ball(2, state.ballPos.x, state.ballPos.y)
      );
      this.onBallStop = (ball) => {
        if (!state.firstBallStop) {
          state.ballPos = ball.position.copy();
          state.firstBallStop = true;
        }

        ball.position.x = state.ballPos.x;
      };
      this.balls.forEach((ball) => ball.setOnStop(this.onBallStop));
    }

    collideWithBricks(bricks) {
      bricks.bricks.forEach((brick) => {
        this.balls.forEach((ball) => {
          const collided = ball.collideWith(brick);
          if (collided) {
            brick.hit();
          }
        });
      });
    }

    collideWithBonusBall(bonusBalls) {
      this.balls.forEach((ball) => {
        bonusBalls.forEach((bonusBall) => {
          const collided = ball.collideWithBonusBall(bonusBall);
          if (collided) bonusBall.hitWithBall();
        });
      });
    }

    get allStopped() {
      return this.balls.every((ball) => ball.velocity.mag() === 0);
    }

    addBalls(state, n) {
      const newBalls = range(n).map(
        (i) => new Ball(2, state.ballPos.x, state.ballPos.y)
      );
      newBalls.forEach((ball) => ball.setOnStop(this.onBallStop));
      this.balls.push(...newBalls);
    }

    async shoot(mousePos, state) {
      for (const ball of this.balls) {
        if (state.ballDowning) return;
        ball.shoot(mousePos);
        await delay(Math.max(50 - ~~(state.ballCount / 10), 10));
      }
    }

    display() {
      this.balls.forEach((ball) => {
        ball.update();
        ball.checkEdges();
        ball.display();
      });
    }

    down() {
      this.balls.forEach((ball) => ball.down());
    }
  }

  class Bricks {
    constructor() {
      this.bricks = [];
      this.particleSystems = new BrickParticleSystems();
    }

    addBricks(state, newBrickIndeces) {
      const newBricks = newBrickIndeces.map(
        (i) => new Brick(state.level, i, 0)
      );
      this.bricks.push(...newBricks);
    }

    display(state) {
      this.bricks.forEach((brick) => {
        brick.update(state);
        brick.display(state);
      });

      this.particleSystems.run();
    }

    break() {
      const brokenBricks = this.bricks.filter((brick) => brick.broken);
      this.particleSystems.addParticleSystem(...brokenBricks);

      this.bricks = this.bricks.filter((brick) => !brick.broken);
    }

    shouldSlideDown(state) {
      return this.bricks[0] && this.bricks[0].shouldMoveDown(state);
    }

    get hitBottom() {
      return this.bricks[0] && this.bricks[0].hitBottom;
    }
  }

  class BonusBalls {
    constructor() {
      this.bonusBalls = [];
    }

    addBonusBalls(state, newBonusBallIndex) {
      this.bonusBalls = [
        ...this.bonusBalls,
        new BonusBall(state.level, newBonusBallIndex, 0),
      ];
    }

    display(state) {
      this.bonusBalls.forEach((bonusBall) => {
        bonusBall.update(state);
        bonusBall.display();
      });
    }

    collideWithBall(balls) {
      this.bonusBalls.forEach((bonusBall) =>
        balls.balls.forEach((ball) => bonusBall.collideWith(ball))
      );
    }

    removeHitBalls() {
      this.bonusBalls = this.bonusBalls.filter(
        (b) => !b.hit || b.y > height
      );
    }

    get hitBallCount() {
      return this.bonusBalls.filter((ball) => ball.hit).length;
    }
  }

  class LocalStorageManager {
    constructor() {
      this.bestScoreKey = "brickBestScore";
      this.storage = window.localStorage;
    }

    getBestScore() {
      return this.storage.getItem(this.bestScoreKey) || 1;
    }

    setBestScore(score) {
      this.storage.setItem(this.bestScoreKey, score);
    }

    setScore(score) {
      this.setBestScore(Math.max(score, this.getBestScore()));
    }
  }

  class GameManager {
    constructor() {
      this.state = {
        ballPos: new Vector(width / 2, height - 100),
        ballMoving: false,
        ballCount: 1,
        ballDowning: false,
        brickMoving: false,
        firstBallStop: true,
        level: 1,
        over: false,
      };

      this.balls = new Balls(this.state);
      this.bricks = new Bricks();
      this.bonusBalls = new BonusBalls();
      this.ballLine = new BallLine();
      this.ui = new UI();
      this.scoreStorage = new LocalStorageManager();
      this.state.bestLevel = this.scoreStorage.getBestScore();

      this.addBallsAndBricks();

      canvas.addEventListener("click", (e) => this.shootBalls(e));
    }

    addBallsAndBricks() {
      const bonusBallCount = this.bonusBalls.hitBallCount;
      const newBrickIndeces = shuffle(range(6)).slice(
        0,
        Math.random() > 0.9 ? randomInt(5) : randomInt(4)
      );
      const newBonusBallIndex = shuffle(
        range(6).filter((i) => !newBrickIndeces.includes(i))
      )[0];

      this.state.ballCount += bonusBallCount;
      this.balls.addBalls(this.state, bonusBallCount);
      this.bricks.addBricks(this.state, newBrickIndeces);
      this.bonusBalls.addBonusBalls(this.state, newBonusBallIndex);
    }

    shootBalls(e) {
      if (
        this.state.ballMoving ||
        this.state.brickMoving ||
        this.state.over
      )
        return;

      this.state.ballPos = null;
      this.state.ballMoving = true;
      this.state.ballDowning = false;
      this.state.firstBallStop = false;

      const { x, y } = Mouse.position;
      this.balls.shoot({ x, y: Math.min(y, 720) }, this.state);
    }

    checkCollision() {
      this.balls.collideWithBricks(this.bricks);
      this.bonusBalls.collideWithBall(this.balls);
      this.bricks.break();
    }

    draw() {
      clear();
      this.ballLine.display(this.state);
      this.balls.display();
      this.bricks.display(this.state);
      this.bonusBalls.display(this.state);
      this.ui.display(this.state);
    }

    run() {
      this.draw();
      this.checkCollision();

      if (this.state.ballMoving && this.balls.allStopped) {
        this.state.ballMoving = false;
        this.state.brickMoving = true;

        this.state.level += 1;
        this.scoreStorage.setScore(this.state.level);
        this.state.bestLevel = this.scoreStorage.getBestScore();

        this.addBallsAndBricks();
      }

      if (this.state.brickMoving) {
        if (!this.bricks.shouldSlideDown(this.state)) {
          this.state.brickMoving = false;
          this.bonusBalls.removeHitBalls();
        }
      }

      if (this.bricks.hitBottom) {
        this.ui.gameOver();
        this.state.over = true;
      }

      window.requestAnimationFrame(() => this.run());
    }

    downBalls() {
      this.state.ballDowning = true;
      this.balls.down();
    }
  }

  canvas.addEventListener("mousemove", (e) => {
    const scale = ctx.scale;
    const offset = ctx.offset;
    const mx = e.pageX - canvas.offsetLeft;
    const my = e.pageY;

    Mouse.position = new Vector(mx, my);
  });

  const gameManager = new GameManager();

  gameManager.run();