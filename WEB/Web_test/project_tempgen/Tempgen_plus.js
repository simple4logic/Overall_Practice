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
  
  for(var i = 1 ; i < 6 ; i++){ //j = roomname, i = timeline
    var rooms = [];

    for(var j = 0; j < 8 ; j++){
      temp = Math.random() * (max - min);
      ans = Math.floor(temp * 10) / 10 + min;
      rooms.push(ans);
      
      objectid = ''.concat(roomname[j],i);
      document.getElementById(objectid).innerText = ans;
    }

    //결과적으로 rooms라는 배열 안에는 지금 특정 시간의 모든 생활관 온도가 기록되어 있음.
    //[1, 8, 6, 7, 5, 3, 4, 2]
    console.log(rooms);
    min_idx = rooms.indexOf(Math.max.apply(null, rooms));
    minid = ''.concat(roomname[min_idx],i);
    console.log(minid);
    document.getElementById("minid").style.color = "blue";
    // maxid = ''.concat(roomname[rooms.indexOf(Math.max(rooms))],i);
    // document.getElementById("maxid").style.color = "red";
    
  }
}


/* 최대 입력할 수 있는 숫자의 길이를 제한하는 함수 */
function handleOnInput(el, maxlength) {
  if(el.value.length > maxlength)  {
    el.value 
      = el.value.substr(0, maxlength);
  }
}