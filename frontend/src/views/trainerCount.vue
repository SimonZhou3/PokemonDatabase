<template>
  <div class="container">
    <button class="btn btn-outline-success" @click="this.switchDisplay">Switch to {{this.$data.nextTable}}</button>
    <div v-if=this.$data.isLeaderboard>
      <h1 class="purples pad-top">Leaderboards</h1>
      <div class="d-flex justify-content-center pad-query">
        <form class="d-flex">
          <input class="form-control me-3" type="number" min=0 id="filter-range" value="0"/>
          <select class="form-control me-3" id="operator">
            <option value=">"> GREATER</option>
            <option value=">="> GREATER OR EQUAL</option>
            <option value="<"> LESS THAN</option>
            <option value=">="> LESS THAN OR EQUAL</option>
            <option value="="> EQUAL</option>
            <option value="<>"> NOT</option>
          </select>
        </form>
        <button class="btn btn-outline-primary" v-on:click="fetchLeaderboardByFilters">Submit</button>
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
          <th scope="row" class="col-4"> {{ trainer.trainer_id }}</th>
          <td> {{ trainer.trainer_name }}</td>
          <td>{{ trainer.pokemon_count }}</td>
        </tr>
        </tbody>
      </table>
    </div>
    <div v-if="this.$data.isCommon">
      <h2 class="pad-top mint">Find Common Pokemons</h2>
      <div class="d-flex justify-content-center">
        <form>
          <select class="form-control me-3" id="gender">
            <option value="">All</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </form>
        <button class="btn btn-outline-primary space-left" v-on:click="fetchPokemonByGender">Find Common Pokemon</button>
      </div>
      <table class="table table-danger mt-5">
        <thead>
        <tr>
          <th scope="col" class="col-4">Pokedex #</th>
          <th scope="col">Pokemon Name</th>
          <th scope="col">Pokemon Sprite</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="pokemon of this.commonPokemonData" :key="pokemon">
          <th scope="row" class="col-4"> {{ pokemon.pokemon_id }}</th>
          <td> {{ pokemon.name }}</td>
          <td><img :src="pokemon.sprite" alt="pokemon_sprite"/></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
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
      isLeaderboard: true,
      isCommon: false,
      nextTable: "Common Pokemon"
    };
  },
  methods: {

    switchDisplay() {
      if (this.$data.nextTable === "Common Pokemon") {
        this.$data.isLeaderboard = false;
        this.$data.isCommon = true;
        this.$data.nextTable = "Leaderboards"
      } else {
        this.$data.isLeaderboard = true;
        this.$data.isCommon = false;
        this.$data.nextTable = "Common Pokemon"
      }
      this.forceRerender()
    },

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
        fetch("http://127.0.0.1:5000/trainer/all?gender=%27" + gender + "%27", {
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
          method: 'GET'
        }).then((response) => response.json()).then((data) => {
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
      this.$data.trainerData = []
      this.forceRerender()

      const filter_range = document.getElementById('filter-range').value
      const operator = document.getElementById('operator').value
      fetch("http://127.0.0.1:5000/trainer/leaderboard?range=" + filter_range + "&operator=" + operator, {
        method: 'GET'
      }).then((response) => response.json()).then((data) => {
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
/* REFERENCE -- https://codepen.io/cssgrid/pen/BaYKdeM*/
.pad-query {
  padding-bottom: 7vh;
}

.pad-top {
  padding-top: 1vh;
}

@font-face {
  font-family: 'Rocher';
  src: url(https://assets.codepen.io/9632/RocherColorGX.woff2);
}

.purples {
  font-family: Rocher;
  base-palette: 6;
}

.mint {
  font-family: Rocher;
  base-palette: 7;
}

.space-left {
  margin-left: 2rem;
}

</style>