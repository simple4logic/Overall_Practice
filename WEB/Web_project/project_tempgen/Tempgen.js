/* gloval variable of roomname */
var roomname = ["경비1-", "경비2-", "정리1-", "정리2-", "하역1-", "하역2-", "본부-", "장비정비-"];

/* 난수 출력하는 메인 함수*/
function printrand() {
  const min = Number(document.getElementById('mininput').value);
  const max = Number(document.getElementById('maxinput').value);

  //잘못 된 값 입력시 배제
  if(max < min){
    window.alert("최대 온도가 최소 온도보다 작을 수는 없습니다!");
    return;
  }
  
  for(var j = 0; j < 8 ; j++){
    for(var i = 1 ; i < 6 ; i++){
      temp = Math.random() * (max - min);
      ans = Math.floor(temp * 10) / 10 + min;
      
      objectid = ''.concat(roomname[j],i); //j = roomname, i = timeline
      document.getElementById(objectid).innerText = ans;
    }
  }
}




/* 최대 입력할 수 있는 숫자의 길이를 제한하는 함수 */
function handleOnInput(el, maxlength) {
  if(el.value.length > maxlength)  {
    el.value 
      = el.value.substr(0, maxlength);
  }
}