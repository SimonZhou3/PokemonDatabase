<template>
  <div class="pane" ref="pane">
    <div class="versionContainer" id="version">
      <div v-for="version of this.allVersions" :key="version">
        <versionEntry
          :data="version"
          :keyVersions="this.$props.versions"
          :selected="this.$props.pokemonData.pokemon_version_id"
          :color="this.$props.color"
          @queryVersion="onQueryVersion"
        />
      </div>
    </div>
    <div class="dataContainer">
      <div class="entryContainer" id="move" ref="move">
      <div class="name">Moves</div>
        <div v-for="move of this.moves" :key="move">
          <dataEntry
            :data="move"
            :color="this.$props.color"
            :type="'Move'"
            @queryData="onQueryData"
          />
        </div>
      </div>
      <div class="entryContainer" id="area" ref="area">
        Area
        <div v-for="area of this.areas" :key="area">
          <dataEntry
            :data="area"
            :color="this.$props.color"
            :type="'Area'"
            @queryData="onQueryData"
          />
        </div>
      </div>
      <div class="entryContainer" id="item" ref="item">
        item
        <div v-for="item of this.items" :key="item">
          <data-entry
            :data="item"
            :color="this.$props.color"
            :type="'Item'"
            @queryData="onQueryData"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import dataEntry from "./dataEntry.vue";
import versionEntry from "./versionEntry.vue";
export default {
  props: ["pokemonData", "versions", "update", "color", "toggle"],
  watch: {
    toggle: function (value) {
      if (value) {
        let pane = this.$refs.pane;
        gsap.to(pane, { top: "100vh", duration: 0.5, ease: "expo" });
      }
    },
  },
  data() {
    return {
      moves: [],
      areas: [],
      items: [],
      allVersions: [],
      refresh: this.$props.update,
      accentColor: this.$props.color,
    };
  },
  components: {
    dataEntry,
    versionEntry,
  },
  methods: {
    onQueryVersion(version_id) {
      this.toggleData(false);
      console.log("switching to version" + version_id);
      this.$emit(
        "query",
        this.$props.pokemonData.pokemon_generic_id,
        version_id
      );
    },
    // onResponse(data) {
    //   this.move = data.data[0].moves;
    //   this.toggleData(true);
    //   console.log(data);
    // },
    toggleData(show) {
      let opacity;
      if (show) {
        opacity = 1;
      } else {
        opacity = 0;
      }
      let move = this.$refs.move;
      let area = this.$refs.area;
      let item = this.$refs.item;
      gsap.to(move, { autoAlpha: opacity, duration: 0.5, ease: "expo" });
      gsap.to(area, {
        autoAlpha: opacity,
        duration: 0.5,
        ease: "expo",
        delay: 0.2,
      });
      gsap.to(item, {
        autoAlpha: opacity,
        duration: 0.5,
        ease: "expo",
        delay: 0.4,
      });
    },
    onQueryData(data, type) {
      this.$emit("queryData", data, type);
    },
  },
  mounted() {
    let pane = this.$refs.pane;
    pane.style.opacity = 1;
    this.moves = this.$props.pokemonData.moves;
    this.areas = this.$props.pokemonData.areas;
    this.items = this.$props.pokemonData.items
    this.allVersions = this.$props.pokemonData.version_list;
    console.log("showing data", this.$props.versions, this.moves, this.area);
    this.toggleData(true);
    gsap.fromTo(
      pane,
      { top: "100vh" },
      { top: "35vh", duration: 1, ease: "expo" }
    );
  },
  updated() {
    this.moves = this.$props.pokemonData.moves;
    this.areas = this.$props.pokemonData.areas;
    this.allVersions = this.$props.pokemonData.version_list;
    console.log("showing data", this.$props.versions, this.moves, this.area);
    this.toggleData(true);
  },
};
</script>

<style scoped>
.pane {
  position: absolute;
  width: 90vw;
  height: 65vh;
  left: 5vw;
  background-color: #ffffff;
  border-radius: 5vh;
  opacity: 0;
  transition: opacity 1s;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  overflow: hidden;
  /* border: 1px solid rgb(0, 129, 54); */

  /* filter: drop-shadow(0px 0px 6px #ebebeb) */
}
.dataContainer {
  position: relative;
  top: 27%;
  /* border: 1px solid blue; */
  height: 80%;
  width: 100%;
}
.entryContainer {
  position: absolute;
  border: 1px solid red;
  width: 30%;
  height: 90%;
  overflow: auto;
}
.entryContainer#move {
  left: 2%;
}
.entryContainer#area {
  left: 35%;
}
.entryContainer#item {
  left: 68%;
}

.versionContainer {
  position: absolute;
  margin-top: 0%;
  /* border: 1px solid red; */
  /* border-radius: 2.5vh; */
  width: 100%;
  height: 25%;
  display: flex;
  margin-left: auto;
  margin-right: auto;
  overflow-y: visible;
  overflow-x: auto;
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
  background: v-bind(accentColor);
  border-radius: 5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: v-bind(accentColor);
}
</style>