<!DOCTYPE html>
<html>
<head>
	<title>Регистрация</title>
	<meta charset="utf-8">
</head>
<body>
<form action="/signin" method="POST">
            Email: <input name="email" type="text" value="{{email}}" />
            <br>
            Username: <input name="login" type="text" value="{{username}}" />
            <br>

            Password: <input name="password" type="password" />
            <p>
                  %if error_msg == "Invalid username":
                  Пользователь с таким именем уже существует
                  %end

                  %if error_msg == "Invalid email":
                  Проверьте правильность введеного Email
                  %end

                  %if error_msg == "Email already exists":
                  Пользователь с таким Email уже существует
                  %end

                  %if error_msg == "Invalid passwords length":
                  Пароль должен быть длиннее 8 символов и короче 20 символов
                  %end

                  %if error_msg == "Invalid passwords case":
                  Пароль должен содержать заглавные и строчные символы
                  %end

                  %if error_msg == "Invalid passwords contain":
                  Пароль должен содержать буквы и цифры
                  %end

                  %if error_msg == "Invalid passwords lang":
                  Пароль должен содержать только латиницу
                  %end

            </p>
            <input value="Signin" type="submit" />
        </form>
</body>
</html>