function printrand() {
  const min = Number(document.getElementById('mininput').value);
  const max = Number(document.getElementById('maxinput').value);

  //잘못 된 값 입력시 배제
  if(max < min){
    window.alert("다시 입력해주세요!");
    return;
  }

  ans = Math.floor(Math.random() * (max - min + 1)) + min;
  
  document.getElementById("result").innerText = ans;
  }
    