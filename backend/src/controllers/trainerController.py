from models.trainer import Trainer
from models.trainedPokemon import TrainedPokemon
from operator import itemgetter
from flask import request,jsonify
import json

class TrainerController:
    @staticmethod
    def listTrainerFormat(trainers):
        arr=[]
        for trainer in trainers:
            vals = {}
            vals['trainer_id']=trainer[0]
            vals['name']=trainer[1]
            vals['gender']=trainer[2]
            arr.append(vals)
        return arr

    @staticmethod
    def trainerFormat(trainer):
        return { "data": [
            {
               'trainer_id': trainer.trainer_id,
               'gender': trainer.gender,
               'name': trainer.name,
               'pokemon': trainer.pokemon
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
            trainer_id = await Trainer.create(data)
            trainer = Trainer(trainer_id)
            await trainer.load()
            return TrainerController.trainerFormat(trainer)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    async def addPokemon(trainer_id, data):
        await TrainedPokemon.create(trainer_id,data)
        return jsonify(success=True)

    @staticmethod
    async def updatePokemon(trainer_id,trained_pokemon_id,data):
        trainedPokemon = TrainedPokemon(trained_pokemon_id)
        await trainedPokemon.load()
        try:
            nickname,level = itemgetter('nickname', 'level')(data)
            trainedPokemon.nickname = nickname
            trainedPokemon.level = level
            await trainedPokemon.update()
        except:
            return jsonify(success=False)

        return jsonify(success=True)

    @staticmethod
    async def removePokemon(trained_pokemon_id):
        trainedPokemon = TrainedPokemon(trained_pokemon_id)
        await trainedPokemon.delete()
        return jsonify(success=True)

    @staticmethod
    async def get(trainer_id):
        print("Get Trainer Called")
        trainer = Trainer(trainer_id)
        await trainer.load()
        return TrainerController.trainerFormat(trainer)


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


    @staticmethod
    async def getHighestStats(range, operator):
        result = await TrainedPokemon.getLeaderboard(range, operator)
        jsonArray = []

        for trainer_data in result:
            jsonObject = {
                'trainer_id': trainer_data[0],
                'trainer_name': trainer_data[1],
                'Pokemon Count': trainer_data[2]
            }
            jsonArray.append(jsonObject)

        return {
            "data": jsonArray
        }