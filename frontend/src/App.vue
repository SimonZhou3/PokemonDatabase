<template>
  <div>
    <SearchBar
      :pokemonList="this.pokemonList"
      :sprite="this.pokemonSprite"
      :received="this.received"
      @querying="queryPokemonGenericData"
      @completed="displayResults"
      ref="searchBar"
    />
    <DataPane
      v-if="this.show"
      :pokemonData="this.pokemonData"
      :versions="this.versionData"
      :update="this.update"
      :color="this.typeColor[this.pokemonTypes[0].type].accent"
      @query="queryPokemonSpecificData"
    />
    <StatPane
      v-if="this.show"
      :stats="this.pokemonStats"
      :color="this.typeColor[this.pokemonTypes[0].type].accent"
    />
    <DescPane
      v-if="this.show"
      :types="this.pokemonTypes"
      :name="this.pokemonName"
      :description="this.pokemonDesc"
      :colors="this.typeColor"
    />
  </div>
</template>

<script>
import { gsap } from "gsap";
import SearchBar from "./components/SearchBar.vue";
import DataPane from "./components/dataPane.vue";
import StatPane from "./components/statsPane.vue";
import DescPane from "./components/descPane.vue";
export default {
  name: "App",
  components: {
    SearchBar,
    DataPane,
    StatPane,
    DescPane,
  },
  data() {
    return {
      received: false,
      show: false,
      pokemonData: null,
      typeColor: {
        normal: { main: "#CC99A8", accent: "#75515B" },
        fighting: { main: "#EF6138", accent: "#994025" },
        flying: { main: "#93B2C7", accent: "#49677D" },
        poison: { main: "#9B69D9", accent: "#5E2D88" },
        ground: { main: "#A96F2E", accent: "#6E491F" },
        rock: { main: "#8B3E21", accent: "#421B0F" },
        bug: { main: "#3B9852", accent: "#1C4B27" },
        ghost: { main: "#906790", accent: "#313469" },
        steel: { main: "#44BD94", accent: "#5F756D" },
        fire: { main: "#FD4C5A", accent: "#A91F27" },
        water: { main: "#86A9FA", accent: "#1552E2" },
        grass: { main: "#27CB4F", accent: "#157A3F" },
        electric: { main: "#FBFB72", accent: "#E3E32B" }, //need dark font
        psychic: { main: "#F81D8F", accent: "#A6296C" },
        ice: { main: "#84D2F7", accent: "#86D2F5" }, //need dark font
        dragon: { main: "#63C9D7", accent: "#448B95" },
        dark: { main: "#5A5979", accent: "#448B95" },
        fairy: { main: "#EA1369", accent: "#971944" },
        unknown: { main: "#A6A8A8", accent: "#AAA8AB" }, //need dark font
        shadow: { main: "#272C3B", accent: "#1B1E28" },
      },
      pokemonList: [],
      pokemonSprite: null,
      pokemonStats: null,
      pokemonTypes: null,
      pokemonName: null,
      pokemonDesc: null,
      versionData: null,
      pokemonColors: null,
      update: 0,
    };
  },
  methods: {
    displayResults() {
      console.log("received query results", this.pokemonData);
      this.show = true;
      this.update += 1;
      let mainColor = this.typeColor[this.pokemonTypes[0].type].main;
      let accentColor = this.typeColor[this.pokemonTypes[0].type].accent;
      // document.getElementById("app").style.backgroundColor =
      // this.typeColor[this.pokemonTypes[0].type].main;
      console.log(mainColor, accentColor);
      let app = document.getElementById("app");
      gsap.to(app, {
        backgroundImage:
          "linear-gradient(" + mainColor + ",  " + accentColor + ")",
      });
      // document.getElementById("app").style.backgroundImage
      //   = "linear-gradient(" + mainColor + ", " + accentColor + ")"
    },
    filterResult(data) {
      // console.log(data)
      let pokemonList = [];
      for (let pokemon of data["data"]) {
        pokemonList.push(pokemon);
      }
      this.pokemonList = pokemonList;
    },
    sortData(data) {
      // console.log(data,versions)
      this.pokemonStats = data.data[0].stat;
      this.pokemonTypes = data.data[0].type;
      this.pokemonData = data.data[0];
      this.pokemonSprite = data.data[0].sprite;
      this.pokemonDesc = data.data[0].description;
      this.pokemonName = data.data[0].name;
      this.update += 1;
    },
    queryPokemonGenericData(pokemon_generic_id) {
      fetch("http://127.0.0.1:5000/pokemon/" + pokemon_generic_id, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          this.received = true;
          this.sortData(data);
        });
    },
    queryPokemonSpecificData(pokemon_generic_id, version_id) {
      fetch(
        "http://127.0.0.1:5000/pokemon/" +
          pokemon_generic_id +
          "?version_id=" +
          version_id,
        {
          method: "GET",
        }
      )
        .then((response) => response.json())
        .then((data) => this.sortData(data));
    },
  },
  mounted() {
    console.log("mounted");
    fetch("http://127.0.0.1:5000/pokemon", {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => this.filterResult(data));
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
  background-image: linear-gradient(#1b1e28, #1b1e28);
  width: 100vw;
  height: 100vh;
  transition: background-image 1s;
  overflow: hidden;
}
</style>
