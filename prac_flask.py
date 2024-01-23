from flask import Flask, render_template

#app이라는 객체를 생성해서 flask를 사용하겠다
app = Flask(__name__)

@app.route('/') #경로 지정
def hello():
    return"hello"

@app.route('/im') #경로 지정
def hello12():
    return"imim"


#파이썬 파일이 실행되는 경로안에 templates 폴더 생성 후 html 파일 넣기
@app.route('/prac')
def py_flask():
    return render_template("test.html")

def main():
    app.run(host='127.0.0.1', debug=False, port='80')
#debug=True 일 경우 오류메세지 출력해 줌

if __name__ == '__main__':
    main()
