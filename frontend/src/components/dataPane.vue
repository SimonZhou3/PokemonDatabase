<template>
  <div class="pane" ref="pane">
    <div class="dataContainer" id="version">
      <div v-for="version of this.allVersions" :key="version">
        <versionEntry
          :data="version"
          :keyVersions="this.$props.versions"
          :selected="this.$props.pokemonData.pokemon_version_id"
          @queryVersion="onQueryVersion"
        />
      </div>
    </div>
    <div class="dataContainer" id="move">
      <div v-for="move of this.moves" :key="move">
        <dataEntry :data="move" />
      </div>
    </div>
    <div class="dataContainer" id="area">Area</div>
    <div class="dataContainer" id="item">item</div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import dataEntry from "./dataEntry.vue";
import versionEntry from "./versionEntry.vue";
export default {
  props: ["pokemonData", "versions"],
  data() {
    return {
      moves: [],
      areas: [],
      items: [],
      allVersions: [],
    };
  },
  components: {
    dataEntry,
    versionEntry,
  },
  methods: {
    onQueryVersion(version_id) {
      fetch(
        "http://127.0.0.1:5000/pokemon/" +
          this.$props.pokemonData.pokemon_generic_id +
          "?version_id=" +
          version_id,
        {
          method: "GET",
        }
      )
        .then((response) => response.json())
        .then((data) => this.onResponse(data));
    },
    onResponse(data) {
        console.log(data)
    }
  },
  mounted() {
    console.log("showing data", this.$props.pokemonData, this.$props.versions);
    let pane = this.$refs.pane;
    pane.style.opacity = 1;
    this.moves = this.$props.pokemonData.moves;
    this.allVersions = this.$props.pokemonData.version_list;
    // console.log(this.moves)
    gsap.fromTo(
      pane,
      { top: "50vh" },
      { top: "15vh", duration: 1, ease: "expo" }
    );
  },
};
</script>

<style scoped>
.pane {
  position: relative;
  width: 90vw;
  height: 65vh;
  left: 5vw;
  background-color: #ffffff;
  border-radius: 5vh;
  opacity: 0;
  transition: opacity 1s;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  /* filter: drop-shadow(0px 0px 6px #ebebeb) */
}
.dataContainer {
  position: relative;
  border: 1px solid red;
  left: 0%;
  width: 30%;
  height: 50vh;
  display: inline-block;
  margin-right: 1%;
  overflow: auto;
  top: -3vh;
}
.dataContainer#version {
  top: -5%;
  width: 99.9%;
  height: 10vh;
  overflow-x: auto;
  overflow-y: hidden;
  white-space: nowrap;
  display: flex;
  margin-bottom: 0.5%;
}
/* width */
::-webkit-scrollbar {
  width: 5px;
}
::-webkit-scrollbar {
  height: 8px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #ffffff;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #cf4444;
  border-radius: 5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgb(255, 77, 77);
}
</style>