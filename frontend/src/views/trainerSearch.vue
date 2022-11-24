<template>
<div>
  <div>
    <SearchBar
        :trainerList="this.trainerList"
        :sprite = "this.trainerSprite"
        :received="this.received"
        @querying="queryTrainerData"
        @completed="displayResults"
        ref="searchBar"
    />
  </div>
  <TrainerDataPane
      v-if="this.show"
      :trainerData="this.trainerData"
      :update="this.update"
      @query="queryTrainerData"
  />
</div>
</template>

<script>

import SearchBar from "../components/trainerSearchBar.vue";
import TrainerDataPane from "@/components/trainerDataPane";

export default {
  name: "App",
  components: {
    TrainerDataPane,
    SearchBar
  },
  data() {
    return {
      received: false,
      show: false,
      trainerData: null,
      trainerList: [],
      trainerName: null,
      trainerGender: null,
      trainerSprite: null,
      trainerPokemon: [],
      update: 0,
    };
  },
  methods: {
    displayResults() {
      console.log("received query results", this.pokemonData);
      this.show = true;
      this.update += 1;
    },

    filterResult(data) {
      let trainerList = [];
      for (let trainer of data["data"]) {
        trainerList.push(trainer);
      }
      this.trainerList = trainerList;
    },

    queryTrainerData(trainer_id) {
      fetch("http://127.0.0.1:5000/trainer/" + trainer_id, {
        method: "GET",
      })
          .then((response) => response.json())
          .then((data) => {
            this.received = true;
            this.sortData(data);
          });
    },

    sortData(data) {
      this.trainerData = data.data[0];
      this.trainerName = data.data[0].name;
      this.trainerGender = data.data[0].gender;
      this.trainerPokemon = data.data[0].pokemon;
      this.trainerSprite = this.trainerGender === 'Male' ? "https://art.pixilart.com/0527c89b86fbcd9.png" : "https://pbs.twimg.com/media/D5mKg__WsAAsAEb.png";
    },
  },

  mounted() {
    console.log("Trainer mounted");
    fetch("http://127.0.0.1:5000/trainer", {
      method: "GET",
    })
        .then((response) => response.json())
        .then((data) => this.filterResult(data));
  }
};

</script>

<style>
body,
html {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: linear-gradient(#1b1e28, #1b1e28);
  width: 100vw;
  height: 100vh;
  transition: background-image 1s;
  overflow: hidden;
}
</style>
