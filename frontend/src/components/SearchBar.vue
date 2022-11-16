<template>
  <div class="barContainer" ref="barContainer">
    <input
      class="search"
      ref="search"
      type="text"
      v-model="this.query"
      placeholder="Search Pokemon"
    />
    <div class="pokeball" ref="pokeball" v-show="this.loading">
      <div class="ballTop" ref="ballTop"></div>
      <div class="ballMid" ref="ballMid"></div>
      <div class="ballCenter" id="outer" ref="ballCenterOuter">
        <div class="ballCenter" id="inner" ref="ballCenterInner"></div>
      </div>
    </div>
    <div class="searchResults" ref="searchResults">
      <div v-for="pokemon of findPokemons" :key="pokemon">
        <PokemonEntry
          :pokemon="pokemon"
          v-if="this.query.length > 1"
          @querying="onQuery"
        />
      </div>
    </div>
  </div>
  <!-- <button class="submit" @click="test">Test</button>
  <button class="submit" v-if="showResults"></button> -->
</template>

<script>
import { gsap } from "gsap";
import PokemonEntry from "./PokemonEntry.vue";
export default {
  name: "SearchBar",
  components: {
    PokemonEntry,
  },
  props: ["pokemonList"],
  data() {
    return {
      query: "",
      loading: false,
    };
  },
  computed: {
    findPokemons() {
      let filteredList = [];
      for (let pokemon of this.$props.pokemonList) {
        if (pokemon.toLowerCase().startsWith(this.query.toLowerCase())) {
          filteredList.push(pokemon);
        }
      }
      return filteredList;
    },
  },
  methods: {
    test() {
      this.showResults = false;
      console.log(this.showResults);
    },
    loadAnimation() {
      let bar = this.$refs.barContainer;
      let input = this.$refs.search;
      let ballTop = this.$refs.ballTop;
      let ballMid = this.$refs.ballMid;
      let ballCenterOuter = this.$refs.ballCenterOuter;
      let ballCenterInner = this.$refs.ballCenterInner;
      input.style.opacity = 0;
      gsap.to(bar, { width: "20vh", duration: 1, ease: "expo" });
      gsap.to(bar, { height: "20vh", duration: 1, ease: "expo" });
      gsap.to(bar, { "border-radius": "10vh", duration: 1, ease: "expo" });
      gsap.to(bar, { top: "40vh", duration: 1, ease: "expo" });
      gsap.to(ballTop, { backgroundColor: "#cf4444" });
      gsap.fromTo(
        ballTop,
        { top: "-55%" },
        { top: "0%", duration: 1, ease: "expo", delay: 0.6 }
      );
      // gsap.to(ballTop, {autoAlpha: 1, delay: 0.7})
      gsap.fromTo(
        ballMid,
        { height: "0%" },
        { height: "8%", duration: 0.5, ease: "expo", delay: 1.1 }
      );
      gsap.fromTo(
        ballCenterOuter,
        { scale: 0 },
        { scale: 1, duration: 0.5, ease: "expo", delay: 1.2 }
      );
      gsap.fromTo(
        ballCenterInner,
        { scale: 0 },
        { scale: 1, duration: 1, ease: "expo", delay: 1.4 }
      );
    },
    onQuery() {
      console.log("querying");
      this.loading = true;
      this.query = "";
      this.loadAnimation();
    },
    resize(height) {
      if (!this.loading) {
        let container = this.$refs.barContainer;
        gsap.to(container, { height: height, duration: 0.2, ease: "expo" });
      }
    },
  },
  mounted() {},
  updated() {
    if (this.query.length > 1) {
      //limit height of container
      let requiredHeight = this.findPokemons.length * 6 + 11;
      if (requiredHeight > 47) {
        requiredHeight = 47;
      }
      let height = requiredHeight.toString() + "vh";
      this.resize(height);
    } else {
      this.resize("10vh");
    }
  },
};
</script>

<style scoped>
.barContainer {
  position: relative;
  background-color: #ffffff;
  width: 65vw;
  height: 10vh;
  top: 45vh;
  margin-left: auto;
  margin-right: auto;
  border-radius: 5vh;
  z-index: 1;
}
.search {
  position: relative;
  width: 64vw;
  height: 9vh;
  top: 0vh;
  margin-bottom: 2%;
  border-radius: 5vh;
  border: 0;
  top: 0.4vh;
  text-align: center;
  font-size: 4vh;
}
input:focus {
  outline: none;
}
.searchResults {
  /* border: 1px solid black; */
  border-radius: 0vh;
  position: relative;
  top: 0%;
  height: 75%;
  width: 90%;
  left: 5%;
  overflow: auto
}
/* width */
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #ffffff;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #cf4444;
  border-radius: 2.5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgb(255, 77, 77);
}


.pokeball {
  position: relative;
  height: 100%;
  width: 100%;
  transform-origin: center;
  transform: translateY(-50%);
  clip-path: circle(10vh at center);
}
.ballTop {
  position: relative;
  background-color: #ffffff;
  height: 50%;
  width: 100%;
  top: -60%;
  opacity: 1;
}
.ballMid {
  position: relative;
  background-color: #000000;
  height: 8%;
  width: 100%;
  top: -4%;
}
.ballCenter {
  position: relative;
  background-color: #000000;
  height: 30%;
  width: 30%;
  border-radius: 50%;
  left: 35%;
  top: -25%;
  transform-origin: center;
}
.ballCenter#inner {
  position: relative;
  background-color: #ffffff;
  height: 60%;
  width: 60%;
  left: 20%;
  top: 20%;
}
</style>
