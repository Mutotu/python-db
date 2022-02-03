from flask import Flask
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

def db_test():
    # dino = models.Dino(
    #     name="Test Dino 3",
    #     type="Testing"
    # )
    # models.db.session.add(dino)
    # models.db.session.commit()
    # 
    # this one is for read all
    # dinos = models.Dino.query.all()
    # print(dinos)
    # 
    # this one is read for one
    # dinos = models.Dino.query.filter_by(name="Test Dino 3").all()
    # print(dinos)
    
    # dino = models.Dino.query.filter_by(id=1).first()
    # print(dino)
    # 
    # to update
    # dino.name = dino.name + ", Jr."
    # models.db.session.add(dino)
    # models.db.session.commit()
    # 
    # to delete
    # dino = models.Dino.query.filter_by(id=1).first()
    # models.db.session.delete(dino)
    # models.db.session.commit()
    # option one
    # return 'ok'
    # option 2
    # return {"name": dinos[0].name,
    #         "type": dinos[0].type
    #         }
    # option 3
    # return dinos[0].to_json()
    # category = models.Category(
    #     name = 'Test 1 Cate 1'
    # )
    # dino = models.Dino(
    #     name = 'T rex',
    #     type = 'Jurarsci'
    # )
    # models.db.session.add(dino)
    # models.db.session.add(category)
    # models.db.session.commit()
    dino = models.Dino.query.filter_by(name='Test Dino 3').first()
    category = models.Category.query.first()
    category.dinos_abc.append(dino)
    # dinos = category.dinos_abc
    # print(dino, category,dinos)
    models.db.session.add(category)
    models.db.session.commit()
    return 'ok'
    


app.route('/db_test', methods=["GET"])(db_test)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)