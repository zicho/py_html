<meta http-equiv="Content-Type" content="text/html;charset=utf-8"> 

<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
$(document).ready(function () {
    // uncomment line under this to make it worksing
    $("#test_btn").click(function(){
    
	python_test();
    });

    $("#math_btn").click(function(){
    
	python_math();
    });
});

function python_test() {
    $.ajax({
    url: "/test.py",
    success: function(response) {
    document.getElementById("output_test").innerHTML = response; 
   }
});
}

function python_math() {
    
	var a = Number(document.getElementById('int_a').value);
	var b = Number(document.getElementById('int_b').value);
	
	if(document.getElementById('add_radio').checked) {
		mode = 'add'
    } else if(document.getElementById('sub_radio').checked) {
		mode = 'sub'
    }
	
	$.ajax({
	url: "/math.py",
	method: "GET",
	data: {a : a, b : b, mode : mode},
    success: function(response) {
	    response = JSON.parse(response);
		
	if(response.success) {	
	
        document.getElementById("output_test").innerHTML = response.result; }
		
	else { alert("Ange heltal!"); }	
    
	}
   
});

}
</script>
</head>
<body>
<center>
<button id="test_btn">Den här knappen gör ett AJAX-call till en<br>python-funktion som väljer ett slumpmässigt namn ur en lista</button>
<br><br>
<form action="/action_page.php">
  Integer A:
  <input type="text" id="int_a" value="0"><br><br>
  Integer B:
  <input type="text" id="int_b" value="0"><br>
</form> 

<form>
  <input id="add_radio" type="radio" name="math" value="add" checked> Addition<br>
  <input id="sub_radio" type="radio" name="math" value="sub"> Subtraktion<br>
</form> 

<button id="math_btn">Den här knappen gör ett AJAX-call till en<br>python-funktion som räknar matte</button>

<br><br>
<div id="output_test"></div>
<br><br>  

</body>
</html>
