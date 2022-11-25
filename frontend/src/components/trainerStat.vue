<template>
  <div background="#212529">
    <van-collapse background="#212529" v-model="activeNames">
      <van-collapse-item background="#212529" padding="0" title="Trainer Stats" name="1">
        <table class="table table-bordered table-striped table-dark">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="pokemon of this.trainerStats" :key="pokemon">
              <th scope="row">{{ pokemon.name }}</th>
              <td>{{ pokemon.count }}</td>
            </tr>
          </tbody>
        </table>
      </van-collapse-item>
    </van-collapse>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  props: {
    trainer_id: String,
  },
  setup() {
    const activeNames = ref(["1"]);
    return { activeNames };
  },
  data() {
    return {
      trainerStats: [{ name: "default", count: 20, pokemon_specific_id: 1 }],
    };
  },
  methods: {
    fetchdata: async function () {
      console.log(this.trainer_id);
      console.log("Fetching stats");
      const URL = `http://127.0.0.1:5000/trainer/${this.trainer_id}/pokemonCount`;

      let data = await fetch(URL, {
        method: "GET",
      });
      data = await data.json();
      return data;
    },
  },
  async beforeMount() {
    this.trainerStats = await this.fetchdata();
    console.log(this.trainerStats);
  },
};
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css");

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
  overflow-y: scroll;
  -ms-overflow-y: scroll;
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

.name-title {
  font-family: "Montserrat", sans-serif;
  font-weight: 900;
  font-size: 4vw;
  line-height: 0;
  color: whitesmoke;
  text-align: center;
  -webkit-text-stroke: 4px whitesmoke;
  text-stroke: 4px whitesmoke;
  -webkit-text-fill-color: transparent;
  text-fill-color: transparent;
  padding-top: 4vh;
  padding-bottom: 4vh;
  background-clip: content-box;
  box-shadow: #212529;
  background-color: #212529;
}

.pane-background {
  background-clip: content-box;
  box-shadow: #212529;
  background-color: #212529;
}
</style>
