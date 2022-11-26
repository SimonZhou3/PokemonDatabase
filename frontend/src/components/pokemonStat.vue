<template>
  <div background="#212529">
    <van-collapse background="#212529" v-model="activeNames">
      <van-collapse-item background="#212529" padding="0" title="Pokemon Area Count Location By Region" name="1">
        <table class="table table-bordered table-striped">
          <thead>
            <tr>
              <th scope="col">Region Name</th>
              <th>Area Count</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="region of this.pokemonStats" :key="region">
              <th scope="row">{{ region.name }}</th>
              <td>{{ region.area_count }}</td>
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
    pokemon_id: String,
  },
  setup() {
    const activeNames = ref(["0"]);
    return { activeNames };
  },
  data() {
    return {
      pokemonStats: [],
    };
  },
  methods: {
    fetchdata: async function () {
      console.log(this.trainer_id);
      console.log("Fetching pokemon stats");
      const URL = `http://127.0.0.1:5000/pokemon/${this.pokemon_id}/regionCount`;

      let data = await fetch(URL, {
        method: "GET",
      });
      data = await data.json();
      return data;
    },
  },
  async beforeMount() {
    this.pokemonStats = await this.fetchdata();
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
  box-shadow: rgba(243, 239, 239, 0.24) 0px 3px 8px;
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
  background-color: #ffffff;
}

.pane-background {
  background-clip: content-box;
  box-shadow: #ffffff;
  background-color: #ffffff;
}
</style>
