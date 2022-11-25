<template>
  <div class="d-flex justify-content-center pad-query">
    <form>
      <input type="number" min=0 id="filter-range" value="0"/>
      <select id="operator">
        <option value=">"> GREATER</option>
        <option value=">="> GREATER OR EQUAL</option>
        <option value="<"> LESS THAN</option>
        <option value=">="> LESS THAN OR EQUAL</option>
        <option value="="> EQUAL</option>
        <option value="<>"> NOT</option>
      </select>
    </form>
    <button class="btn btn-primary" v-on:click="fetchLeaderboardByFilters"> Submit Query</button>
  </div>

  <table class="table table-danger">
    <thead>
    <tr>
      <th scope="col" class="col-4">trainer ID</th>
      <th scope="col">trainer name</th>
      <th scope="col">Pokemon Obtained</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="trainer of this.trainerData" :key="trainer">
    <th scope="row" class="col-4"> {{trainer.trainer_id}}</th>
      <td> {{trainer.trainer_name}}</td>
      <td>{{trainer.pokemon_count}}</td>
    </tr>
    </tbody>
  </table>
  <div class="d-flex justify-content-center pad-top">
    <form>
      <select id="gender">
        <option value="">All</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>
      </form>
    <button class="btn btn-primary" v-on:click="fetchPokemonByGender">Find Common Pokemon</button>
    </div>
    <table class="table table-danger">
        <thead>
        <tr>
          <th scope="col" class="col-4">Pokedex #</th>
          <th scope="col">Pokemon Name</th>
          <th scope="col">Pokemon Sprite</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="pokemon of this.commonPokemonData" :key="pokemon">
          <th scope="row" class="col-4"> {{pokemon.pokemon_id}}</th>
          <td> {{pokemon.name}}</td>
          <td><img :src="pokemon.sprite" alt="pokemon_sprite" /></td>
        </tr>
        </tbody>
      </table>
</template>

<script>
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import {nextTick} from "vue";

export default {

  data() {
    return {
      trainerData: [],
      commonPokemonData: [],
    };
  },
  methods: {

    async forceRerender() {
      this.renderComponent = false;
      await nextTick();
      this.renderComponent = true;
      console.log("rerendered...");
    },

    fetchPokemonByGender() {
      console.log('entering division')
      const gender = document.getElementById('gender').value;
      const isSpecified = (gender !== "")
      if (isSpecified) {
        fetch("http://127.0.0.1:5000/trainer/all?gender=%27"+gender + "%27",{
          method: "GET",
        }).then((response) => response.json()).then((data) => {
          this.$data.commonPokemonData = []
          for (const pokemon of data["data"]) {
            this.$data.commonPokemonData.push(pokemon)
          }
          this.forceRerender();
        })
      } else {
        fetch("http://127.0.0.1:5000/trainer/all", {
          method:'GET'
        }).then ((response) => response.json()).then((data) => {
          this.$data.commonPokemonData = []
          for (const pokemon of data["data"]) {
            this.$data.commonPokemonData.push(pokemon)
          }
          this.forceRerender();
        })
      }
    },

    fetchLeaderboardByFilters() {
      console.log('entering query')
      const filter_range = document.getElementById('filter-range').value
      const operator = document.getElementById('operator').value
      fetch("http://127.0.0.1:5000/trainer/leaderboard?range="+filter_range+"&operator="+operator, {
        method:'GET'
      }).then ((response) => response.json()).then((data) => {
        this.$data.trainerData = []
        for (const trainer of data["data"]) {
          this.$data.trainerData.push(trainer)
        }
        this.forceRerender();
      })
    }
    },


  };
</script>

<style>

.pad-query {
  padding-bottom: 7vh;
}
.pad-top {
  padding-top: 10vh;
}
</style>