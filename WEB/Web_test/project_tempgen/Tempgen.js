function printrand() {
  const min = Number(document.getElementById('mininput').value);
  const max = Number(document.getElementById('maxinput').value);

  //잘못 된 값 입력시 배제
  if(max < min){
    window.alert("다시 입력해주세요!");
    return;
  }

  var roomname = ["경비1-", "경비2-", "정리1-", "정리2-", "하역1-", "하역2-", "본부-", "장비정비-"];
  
  for(var j = 0; j < 8 ; j++){
    for(var i = 1 ; i < 6 ; i++){
      temp = Math.random() * (max - min);
      ans = Math.floor(temp * 10) / 10 + min;
      objectid = ''.concat(roomname[j],i);
      document.getElementById(objectid).innerText = ans;
    }
  }
}