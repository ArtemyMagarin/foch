<!DOCTYPE html>
<html>
<head>
	<title>Вход</title>
	<meta charset="utf-8">
</head>
<body>
<form action="/login" method="POST">
            Username: <input name="login" type="text" value="{{login}}" />
            <br>

            Password: <input name="password" type="password" />
            <p 
            % if pass_valid:
            style="display: none"
            % end
            >Пароль неверен</p>
            <input value="Login" type="submit" />
            <a href="/signin" >Signin</a>
        </form>
</body>
</html>