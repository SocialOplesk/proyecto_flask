from flask import Flask, jsonify, request

app = Flask(__name__)

user_list = ["foo","bar","baz"]


@app.route("/users", methods=["GET"])
def users():
    return jsonify({
        "payload":user_list
    });
    

@app.route("/user/", methods=["GET"])
def user():
    name = request.args.get("name")
    cb = lambda i : i == name
    
    try: 
        capture = list(filter(cb,user_list))[0]
     
        return jsonify({
            "payload":capture
        })
    except:
        return jsonify({
            "payload":"user not found"
        })
            

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
