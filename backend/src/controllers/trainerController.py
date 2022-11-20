from models.trainer import Trainer
from operator import itemgetter
from flask import request,jsonify
class TrainerController:
    @staticmethod
    def listTrainerFormat(trainers):
        arr=[]
        for trainer in trainers:
            vals = {}
            vals['trainer_id']=trainer[0]
            vals['name']=trainer[1]
            arr.append(vals)
        return arr

    @staticmethod
    def trainerFormat(trainer):
        return { "data": [
            {
               'trainer_id': trainer.trainer_id,
               'name': trainer.name
            }]}


    @staticmethod
    async def list():
        print("List trainer Called")
        trainers = await Trainer.listTrainers()
        result = TrainerController.listTrainerFormat(trainers)
        return { "data" : result}

    @staticmethod
    async def create(data):
        try:
            name = itemgetter('name')(data)
            print(name)
            trainer_id = await Trainer.create(name)
            trainer = Trainer(trainer_id)
            await trainer.load()
            return TrainerController.trainerFormat(trainer)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    async def get(pokemon_id):
        print("Get Trainer Called")
        return None

    
  

    @staticmethod
    async def update(trainer_id,data):
        try:
            trainer = Trainer(trainer_id)
            print(trainer_id)
            await trainer.update(data)
            return TrainerController.trainerFormat(trainer)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    async def delete(trainer_id):
        trainer = Trainer(trainer_id)
        await trainer.delete()
        return jsonify(sucess=True)