header = input("Type a header : ")
par = input("Type a paragraph : ")

content = '''
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Testing HTML/CSS</title>
	<style type="text/css">
		body {
			font-family: consolas;
			text-align: center;
		}
		p {
			color:red;
			font-size: 40px;
		}
	</style>
</head>
'''

content += f'''
<body>
	<h1>{header}</h1>
	<p>{par}</p>
</body>
</html>
'''

f = open("index.html", "w").write(content)
