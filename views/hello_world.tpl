<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
</head>

<body>
<p>
Welcome {{username}}
<p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<p>
<form action="/favorite_sport" method="POST">
What is your favorite sport?
<input type="text" name="sport" size="40" value=""><br>
<input type="submit" value="Submit"
</form>
</body>
</html>
