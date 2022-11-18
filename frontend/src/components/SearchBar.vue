<template>
  <div>
    <div class="barContainer" ref="barContainer">
      <input
        class="search"
        ref="search"
        type="text"
        v-model="this.query"
        placeholder="Search Pokemon"
        v-if="!loading"
      />
      <div class="pokeball" ref="pokeball" v-show="this.loading">
        <div class="ballTop" ref="ballTop"></div>
        <div class="ballMid" ref="ballMid"></div>
        <div class="ballCenter" id="outer" ref="ballCenterOuter">
          <div class="ballCenter" id="inner" ref="ballCenterInner"></div>
        </div>
        <div class="ballBottom" ref="ballBot"></div>
      </div>
      <div class="searchResults" ref="searchResults">
        <div v-for="pokemon of findPokemons" :key="pokemon">
          <PokemonEntry
            :pokemon="pokemon"
            v-if="this.query.length > 1"
            @querying="onQuery"
            @received="onReceive(data)"
          />
        </div>
      </div>
    </div>
    <button class="debug" @click="test">Mock Complete</button>
  </div>
</template>

<script>
import { gsap } from "gsap";
// import { InertiaPlugin } from "gsap/InertiaPlugin.min.js"
// gsap.registerPlugin(InertiaPlugin)
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
      loaded: false,
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
      this.loaded = true;
    },
    onReceive(data) {
      this.loaded = true
      this.$emit("received", data)
    },
    showPokemon() {
      let pokeball = this.$refs.pokeball;
      let ballTop = this.$refs.ballTop;
      let ballMid = this.$refs.ballMid;
      let ballCenterOuter = this.$refs.ballCenterOuter;
      let ballCenterInner = this.$refs.ballCenterInner;
      let ballBot = this.$refs.ballBot;
      gsap.to(ballCenterInner, {
        scale: 0,
        duration: 0.2,
        ease: "expo",
      });
      gsap.to(ballCenterOuter, {
        scale: 0,
        duration: 0.2,
        ease: "expo",
        delay: 0.2,
      });
      gsap.to(ballMid, {
        top: "-60%",
        duration: 0.2,
        ease: "expo",
        delay: 0.4,
      });
      gsap.to(ballTop, {
        top: "-55%",
        duration: 0.2,
        ease: "expo",
        delay: 0.4,
        onComplete: () => {
          this.$emit("completed");
        },
      });
      gsap.to(ballBot, { scale: 10, duration: 0.2, delay: 0.4 });

      gsap.to(pokeball, {
        top: "-35vh",
        duration: 1,
        ease: "expo",
        delay: 0.5,
      });
      //TODO: display pokemon picture
    },
    stopAnimation() {
      if (this.loaded) {
        console.log("stopping animation", this.loaded);
        let all = gsap.exportRoot();
        gsap.to(all, { timeScale: 0 });
        let pokeball = this.$refs.pokeball;
        gsap.to(pokeball, {
          rotate: 0,
          duration: 0.5,
          ease: "elastic",
          onComplete: this.showPokemon,
        });
      }
    },
    waitForResults() {
      console.log("waiting for query to complete");
      this.$refs.barContainer.style.backgroundColor = "#00000000";
      let pokeball = this.$refs.pokeball;
      pokeball.style.transformOrigin = "bottom";
      gsap.to(pokeball, { rotation: 20, duration: 0.2, ease: "expo" });
      gsap.to(pokeball, {
        rotation: 0,
        duration: 1,
        ease: "elastic",
        repeat: -1,
        yoyo: true,
        delay: 0.3,
        onRepeat: () => {
          this.stopAnimation();
        },
      });
    },
    loadAnimation() {
      let bar = this.$refs.barContainer;
      let input = this.$refs.search;
      let ballTop = this.$refs.ballTop;
      let ballMid = this.$refs.ballMid;
      let ballCenterOuter = this.$refs.ballCenterOuter;
      let ballCenterInner = this.$refs.ballCenterInner;
      input.style.opacity = 0;
      gsap.to(bar, { width: "20vh", duration: 0.9, ease: "expo" });
      gsap.to(bar, { height: "20vh", duration: 0.9, ease: "expo" });
      gsap.to(bar, { "border-radius": "10vh", duration: 1, ease: "expo" });
      gsap.to(bar, { top: "40vh", duration: 1, ease: "expo" });
      gsap.fromTo(
        ballTop,
        { top: "-55%" },
        { top: "0%", duration: 1, ease: "expo", delay: 0.8 }
      );

      gsap.fromTo(
        ballMid,
        { height: "0%" },
        { height: "8%", duration: 0.5, ease: "expo", delay: 1.2 }
      );
      gsap.fromTo(
        ballCenterOuter,
        { scale: 0 },
        { scale: 1, duration: 0.5, ease: "expo", delay: 1.3 }
      );
      gsap.fromTo(
        ballCenterInner,
        { scale: 0 },
        {
          scale: 1,
          duration: 1,
          ease: "expo",
          delay: 1.5,
          onComplete: this.waitForResults,
        }
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
  overflow: auto;
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
  transform: translateY(0%);
  clip-path: circle(10vh at center);
  
}
.ballTop {
  position: relative;
  background-color: #cf4444;
  height: 50%;
  width: 110%;
  top: -60%;
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
.ballBottom {
  position: relative;
  background-color: #ffffff;
  height: 50%;
  width: 100%;
  top: -35%;
  z-index: -1;
}
.debug {
  position: absolute;
  left: 0%;
  top: 0%;
}
</style>
