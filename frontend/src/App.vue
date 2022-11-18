<template>
  <SearchBar :pokemonList="this.pokemonList" @received="compileData(data)" @completed="displayResults" />
  <DataPane v-if="this.received" />
  <StatPane v-if="this.received"/>
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
    };
  },
  methods: {
    displayResults() {
      console.log("received query results");
      this.received = true;
      document.getElementById("app").style.backgroundColor =
        this.typeColor["ice"];
    },
    sortResult(data) {
      // console.log(data)
      let pokemonList = []
      for (let pokemon of data['data']) {
        pokemonList.push(pokemon)
      }
      this.pokemonList = pokemonList
      // console.log(this.pokemonList)
    },
    compileData(data) {
      console.log(data)
    }
  },
  mounted() {
    console.log("mounted")
    fetch("http://127.0.0.1:5000/pokemon", {
      method: "GET",
    }
    ).then((response) => response.json())
    .then((data) => this.sortResult(data))
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
}
</style>
