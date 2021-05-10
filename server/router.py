from flask import Flask, render_template
#python -m pip install flask

#서버 실행
#python router.py


# 1. Flask 객체 생성
app = Flask(__name__)



# 2. 라우터 함수 만들기

#http1.1 => 요청메서드 방식 4가지 방식
#GET(SELECT), POST(INSERT), DELETE(DELETE), PUT(UPDATE)

#Data를 응답
@app.route("/", methods=["GET"])
def home():
    # 파일의 위치는 templates 폴더 안!!
    return render_template("home.html")


#@app.route("/board")
#def detail():
#    return "board"


#Data를 응답
@app.route("/board/<id>")
def detail(id):
    return "board"+id



# 해당 파일이 직접 호출되었을때
if __name__=="__main__":
    app.run(
        host="0.0.0.0", #내서버가 어느아이피에 공개될껀지 전체공개
        port=5000,
        debug=True
    )