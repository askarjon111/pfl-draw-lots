var n = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
var a = document.getElementsByClassName('item');
for (i = 0; i <= a.length -1; i++) {
	  if (!(String(a[i].innerHTML) in n)){
	  	if (a[i].innerHTML!= "14"){
    		a[i].className=
    	}
    	else{
	  	a[i].style.fontSize = '1vw';
	  }
}
	  else{
	  	a[i].style.fontSize = '1vw';
	  }

	
}