<template>
  <div>
    <SearchBar
      :pokemonList="this.pokemonList"
      :sprite="this.pokemonSprite"
      :received="this.received"
      @querying="queryPokemonGenericData"
      @completed="displayResults"
      @reset="togglePanes"
      @resetComplete="onReset"
      ref="searchBar"
    />
    <DataPane
      v-if="this.show"
      :pokemonData="this.pokemonData"
      :versions="this.versionData"
      :update="this.update"
      :color="this.typeColor[this.pokemonTypes[0].type]"
      :toggle="this.reset"
      @query="queryPokemonSpecificData"
      @queryData="queryMoveAreaItem"
    />
    <StatPane
      v-if="this.show"
      :stats="this.pokemonStats"
      :color="this.typeColor[this.pokemonTypes[0].type]"
      :toggle="this.reset"
    />
    <DescPane
      v-if="this.show"
      :types="this.pokemonTypes"
      :name="this.pokemonName"
      :description="this.pokemonDesc"
      :colors="this.typeColor"
      :toggle="this.reset"
    />
  </div>
</template>

<script>
import { gsap } from "gsap";
import SearchBar from "../components/SearchBar.vue";
import DataPane from "../components/dataPane.vue";
import StatPane from "../components/statsPane.vue";
import DescPane from "../components/descPane.vue";
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
        normal: { main: "#CC99A8", accent: "#75515B", text_accent: "#ffffff"},
        fighting: { main: "#EF6138", accent: "#994025", text_accent: "#ffffff"},
        flying: { main: "#93B2C7", accent: "#49677D", text_accent: "#ffffff"},
        poison: { main: "#9B69D9", accent: "#5E2D88", text_accent: "#ffffff"},
        ground: { main: "#A96F2E", accent: "#6E491F", text_accent: "#ffffff"},
        rock: { main: "#8B3E21", accent: "#421B0F", text_accent: "#ffffff"},
        bug: { main: "#3B9852", accent: "#1C4B27", text_accent: "#ffffff"},
        ghost: { main: "#906790", accent: "#313469" , text_accent: "#ffffff"},
        steel: { main: "#44BD94", accent: "#5F756D", text_accent: "#ffffff"},
        fire: { main: "#FD4C5A", accent: "#A91F27", text_accent: "#ffffff"},
        water: { main: "#86A9FA", accent: "#1552E2", text_accent: "#ffffff"},
        grass: { main: "#27CB4F", accent: "#157A3F", text_accent: "#ffffff"},
        electric: { main: "#FBFB72", accent: "#E3E32B" , text_accent: "#000000"}, //need dark font
        psychic: { main: "#F81D8F", accent: "#A6296C", text_accent: "#ffffff"},
        ice: { main: "#84D2F7", accent: "#75C3DB" , text_accent: "#000000"}, //need dark font
        dragon: { main: "#63C9D7", accent: "#448B95", text_accent: "#ffffff"},
        dark: { main: "#448B95", accent: "#5A5979",  text_accent: "#ffffff"},
        fairy: { main: "#EA1369", accent: "#971944", text_accent: "#ffffff"},
        unknown: { main: "#A6A8A8", accent: "#AAA8AB" , text_accent: "#000000"}, //need dark font
        shadow: { main: "#272C3B", accent: "#1B1E28", text_accent: "#ffffff"},
      },
      pokemonList: [],
      pokemonSprite: null,
      pokemonStats: null,
      pokemonTypes: null,
      pokemonName: null,
      pokemonDesc: null,
      versionData: null,
      pokemonColors: null,
      reset: false,
      update: 0,
    };
  },
  methods: {
    togglePanes() {
      console.log("hidding all panes");
      this.reset = true;
      let app = document.getElementById("app");
      gsap.to(app, {
        backgroundImage: "linear-gradient(#1b1e28, #1b1e28)",
      });

      // this.update++;
      // let data = this.$refs.dataPane
      // let stats = this.$refs.statPane
      // // let desc = this.$refs.DescPane

      // gsap.fromTo(data, {top: "0vh"}, {top: "100vh", duration: 1, ease: "expo"})
      // gsap.to(stats, {left: "-50vw", duration: 1, ease: "expo"})
    },
    onReset() {
      window.location.reload();
      // this.received = false;
      // this.show = false;
      // this.reset = false;
    },
    displayResults() {
      console.log("received query results", this.pokemonData);
      this.show = true;
      this.update += 1;
      let mainColor;
      let accentColor;
      if (this.pokemonTypes.length > 1) {
        mainColor = this.typeColor[this.pokemonTypes[0].type].main;
        accentColor = this.typeColor[this.pokemonTypes[1].type].accent;
      } else {
        mainColor = this.typeColor[this.pokemonTypes[0].type].main;
        accentColor = this.typeColor[this.pokemonTypes[0].type].accent;
      }
      // document.getElementById("app").style.backgroundColor =
      // this.typeColor[this.pokemonTypes[0].type].main;
      // console.log(mainColor, accentColor);
      let app = document.getElementById("app");
      gsap.to(app, {
        backgroundImage:
          "linear-gradient(" + mainColor + ",  " + accentColor + ")",
      });

      // let reset = this.$refs.reset;
      // gsap.fromTo(reset, {y: 0} , {y: 10, duration: 0.5, ease: "expo"})
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
    queryMoveAreaItem(data, type) {
      console.log(data, type);
      if (type == "Move") {
        fetch("http://127.0.0.1:5000/move/" + data.move_id, {
          method: "GET",
        })
          .then((response) => response.json())
          .then((data) => console.log(data));
      }
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
  font-family: "Noto Sans Symbols", sans-serif;
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
