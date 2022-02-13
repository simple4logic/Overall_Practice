function printrand() {
  const min = Number(document.getElementById('mininput').value);
  const max = Number(document.getElementById('maxinput').value);

  //잘못 된 값 입력시 배제
  if(max < min){
    window.alert("다시 입력해주세요!");
    return;
  }

  var roomname = ["경비1-", "경비2-", "하역1-", "하역2-", "본 부-", "장비정비-", "정리1-", "정리2-"];
  
  for(var i = 1 ; i < 6 ; i++){
    temp = Math.random() * (max - min);
    ans = Math.floor(temp * 10) / 10 + min;
    objectid = "경비1-".concat(i);
    document.getElementById(objectid).innerText = ans;
  }

}
    