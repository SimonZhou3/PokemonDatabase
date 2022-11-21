<template>
<div>
  <SearchBar :pokemonList="this.pokemonList" @received="sortData" @completed="displayResults" />
  <DataPane v-if="this.received" :pokemonData="this.pokemonData" :versions="this.versionData"/>
  <StatPane v-if="this.received" :stats="this.pokemonStats"/>
</div>
</template>

<script>
import SearchBar from "./components/SearchBar.vue";
import DataPane from "./components/dataPane.vue";
import StatPane from "./components/statsPane.vue";
export default {
  name: "App",
  components: {
    SearchBar,
    DataPane,
    StatPane,
  },
  data() {
    return {
      received: false,
      pokemonData: null,
      typeColor: {
        normal: "#CC99A8",
        fighting: "#EF6138",
        flying: "#93B2C7",
        poison: "#9B69D9",
        ground: "#A96F2E",
        rock: "#8B3E21",
        bug: "#3B9852",
        ghost: "#906790",
        steel: "#44BD94",
        fire: "#FD4C5A",
        water: "#86A9FA",
        grass: "#27CB4F",
        electric: "#FBFB72",
        psychic: "#F81D8F",
        ice: "#84D2F7",
        dragon: "#63C9D7",
        dark: "#5A5979",
        fairy: "#EA1369",
        unknown: "#A6A8A8",
        shadow: "#1F2024",
      },
      pokemonList: [],
      pokemonStats: null,
      pokemonTypes: null,
      versionData: null,
    };
  },
  methods: {
    displayResults() {
      console.log("received query results");
      this.received = true;
      document.getElementById("app").style.backgroundColor =
        this.typeColor[this.pokemonTypes[0].type];
    },
    filterResult(data) {
      // console.log(data)
      let pokemonList = []
      for (let pokemon of data['data']) {
        pokemonList.push(pokemon)
      }
      this.pokemonList = pokemonList
    },
    sortData(data, versions) {
      // console.log(data,versions)
      this.pokemonStats = data.data[0].stat
      this.pokemonTypes = data.data[0].type
      this.pokemonData = data.data[0]
      this.versionData = versions
    }
  },
  mounted() {
    console.log("mounted")
    fetch("http://127.0.0.1:5000/pokemon", {
      method: "GET",
    }
    ).then((response) => response.json())
    .then((data) => this.filterResult(data))
  },
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
  background-color: #1b1e28;
  width: 100vw;
  height: 100vh;
  transition: background-color 1s;
  overflow: hidden;
}
</style>
