<template>
<div v-if="this.$props.isLoaded">
  <div class="pane" ref="pane">
    <div class="d-grid h-100 pane-background">
      <button class="btn btn-outline-light" data-bs-toggle="modal" data-bs-target="#addModal">
        <i class="bi bi-plus"> Add </i>
      </button>
      <div class="d-flex justify-content-center">
        <h2 class="name-title justify-content-center">
          {{ this.name }}
        </h2>
      </div>
      <div>
        <TrainerStat :trainer_id="this.$props.trainerData.trainer_id"></TrainerStat>
      </div>
      <table class="table table-bordered table-striped table-dark" v-if="renderComponent">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th>Version</th>
            <th>Nickname</th>
            <th>Level</th>
            <th>Sprite</th>
            <th>Operations</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="pokemon of this.pokemon" :key="pokemon">
            <th scope="row">{{ pokemon.name }}</th>
            <td>{{ pokemon.version }}</td>
            <td>{{ pokemon.nickname != null ? pokemon.nickname : "--" }}</td>
            <td>{{ pokemon.level }}</td>
            <td><img :src="pokemon.sprite" alt="pokemon_sprite" /></td>
            <td>
              <div class="d-flex justify-content-evenly">
                <button
                  class="btn btn-outline-light"
                  data-bs-toggle="modal"
                  data-bs-target="#editModal"
                  v-on:click="editForm(pokemon.trained_pokemon_id)"
                >
                  <i class="bi bi-pencil-fill"> Edit</i>
                </button>
                <button
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#deleteModal"
                  v-on:click="deleteForm(pokemon.trained_pokemon_id, pokemon.trainer_id)"
                >
                  <i class="bi bi-trash"> Delete</i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <!-- Edit Modal Pop-up -->
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="editModalLabel">Edit Pokemon</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <input type="hidden" value="" id="update-pokemon-id" />
            <input type="hidden" value="" id="update-trainer-id" />
            <div class="mb-3">
              <label for="pokemon-name" class="form-label">Name</label>
              <input class="form-control" id="pokemon-name" disabled />
            </div>
            <div class="mb-3">
              <label for="version-name" class="form-label">Version</label>
              <input type="form-control" class="form-control" id="version-name" disabled />
            </div>
            <div class="mb-3">
              <label for="nickname" class="form-label">Nickname</label>
              <input class="form-control" id="nickname" />
            </div>
            <div class="mb-3">
              <label for="level" class="form-label">Level</label>
              <input type="number" class="form-control" id="level" min="1" max="100" required />
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-primary" v-on:click="updatePokemon()" data-bs-dismiss="modal">
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Delete Modal Pop-up -->
  <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="deleteModalLabel">Delete Pokemon</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <input type="hidden" value="" id="delete-pokemon-id" />
          <input type="hidden" value="" id="trainer-id" />
          Are you sure you want to delete this?
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" v-on:click="deletePokemon()" data-bs-dismiss="modal">
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Add Modal Page 1 Pop-up -->
  <div class="modal fade" id="addModal" tabindex="-1" aria-labelledby="addModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="addModalLabel">Add Pokemon</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="pokemon-name" class="form-label">Name</label>
            <select class="form-control" id="add-pokemon-name">
              <option
                v-for="pokemon in this.$props.allPokemon"
                v-bind:key="pokemon.pokemon_id"
                :value="pokemon.pokemon_id"
              >
                {{ pokemon.name }}
              </option>
            </select>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button
            type="button"
            class="btn btn-primary"
            v-on:click="fetchVersion()"
            data-bs-dismiss="modal"
            data-bs-toggle="modal"
            data-bs-target="#addModal2"
          >
            next
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Add Modal page 2 -->
  <div class="modal fade" id="addModal2" tabindex="-1" aria-labelledby="addModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="addModal2Label">Add Pokemon</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label class="form-label">Version</label>
            <select class="form-control" id="add-version">
              <option
                v-for="version in this.$data.currentTrainedPokemonVersion"
                v-bind:key="version.version_id"
                :value="version.version_id"
              >
                {{ version.name }}
              </option>
            </select>
          </div>
          <div class="mb-3">
            <label for="add-nickname" class="form-label">Nickname</label>
            <input class="form-control" id="add-nickname" />
          </div>
          <div class="mb-3">
            <label for="add-level" class="form-label">Level</label>
            <input type="number" class="form-control" id="add-level" required />
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button
            type="button"
            class="btn btn-primary"
            data-bs-dismiss="modal"
            v-on:click="readDataAndAddTrainedPokemon"
          >
            Add Pokemon
          </button>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { nextTick } from "vue";
import TrainerStat from "./trainerStat.vue";

export default {
  props: ["trainerData", "allPokemon", "isLoaded"],
  data() {
    return {
      name: null,
      gender: null,
      pokemon: [],
      trainer_id: null,
      renderComponent: true,
      currentTrainedPokemonVersion: [],
    };
  },
  components: {
    TrainerStat,
  },
  methods: {
    readDataAndAddTrainedPokemon() {
      console.log(this.trainer_id);
      const pokemon_field = document.getElementById("add-pokemon-name");
      const version_field = document.getElementById("add-version");
      const version_id = version_field.value;
      const pokemon_id = pokemon_field.value;
      const nickname = document.getElementById("add-nickname").value;
      const level = document.getElementById("add-level").value;
      const pokemon_name = pokemon_field.options[pokemon_field.selectedIndex].text;
      const version_name = version_field.options[version_field.selectedIndex].text;
      console.log(pokemon_name);
      console.log(version_name);

      fetch("http://127.0.0.1:5000/pokemon/" + pokemon_id + "?version_id=" + version_id, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          let pokemon_specific_id = Number(data["data"][0]["pokemon_specific_id"]);
          let sprite = data["data"][0]["sprite"];

          fetch("HTTP://127.0.0.1:5000/trainer/" + this.trainer_id + "/pokemon", {
            method: "POST",
            body: JSON.stringify({
              pokemon_specific_id: Number(pokemon_specific_id),
              nickname: nickname == null ? "--" : nickname,
              level: Number(level),
            }),
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((response) => response.json())
            .then((data) => {
              let insertedPokemon = {
                level: Number(level),
                name: pokemon_name,
                nickname: nickname,
                pokemon_specific_id: pokemon_specific_id,
                sprite: sprite,
                version: version_name,
                trainer_id: this.trainer_id,
                trained_pokemon_id: data["data"][0]["trained_pokemon_id"],
              };
              console.log(insertedPokemon);
              this.$data.pokemon.push(insertedPokemon);
              this.forceRerender();
            });
        });
    },

    fetchVersion() {
      console.log("enter fetch version");
      const pokemon_id = document.getElementById("add-pokemon-name").value;
      console.log(pokemon_id);
      fetch("http://127.0.0.1:5000/pokemon/" + pokemon_id, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data["data"][0]["version_list"]);
          for (const version of data["data"][0]["version_list"]) {
            console.log("DEBUGGING: " + version.name);
            this.$data.currentTrainedPokemonVersion.push(version);
          }
          this.forceRerender();
        });
    },

    async forceRerender() {
      this.renderComponent = false;
      await nextTick();
      this.renderComponent = true;
      console.log("rerendered...");
      console.log(this.$data.pokemon);
    },

    updatePokemon() {
      console.log("enter update");
      const update_pokemon_id = document.getElementById("update-pokemon-id").value;
      const update_trainer_id = document.getElementById("update-trainer-id").value;
      const nickname_field_value = document.getElementById("nickname").value;
      const level_field_value = document.getElementById("level").value;
      console.log("p_id: " + update_pokemon_id);
      console.log("tr_id: " + update_trainer_id);
      fetch("http://127.0.0.1:5000/trainer/" + update_trainer_id + "/pokemon/" + update_pokemon_id, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          nickname: nickname_field_value,
          level: Number(level_field_value),
        }),
      }).then(() => {
        let index = -1;
        for (let i = 0; i < this.pokemon.length; i++) {
          console.log("test: " + this.pokemon[i].trained_pokemon_id);
          if (this.pokemon[i].trained_pokemon_id === Number(update_pokemon_id)) {
            index = i;
            break;
          }
        }
        let storePokemon = this.pokemon[index];
        storePokemon.level = level_field_value;
        storePokemon.nickname = nickname_field_value;
        this.$data.pokemon.splice(index, 1);
        this.$data.pokemon.push(storePokemon);
        this.forceRerender();
      });
    },

    deletePokemon() {
      console.log("enter delete");
      const delete_pokemon_id = document.getElementById("delete-pokemon-id").value;
      const trainer_id = document.getElementById("trainer-id").value;
      fetch("http://127.0.0.1:5000/trainer/" + trainer_id + "/pokemon/" + delete_pokemon_id, {
        method: "DELETE",
      }).then(() => {
        let index = -1;
        console.log("delete index id: " + delete_pokemon_id);
        for (let i = 0; i < this.pokemon.length; i++) {
          console.log("test: " + this.pokemon[i].trained_pokemon_id);
          console.log("LOOKING FOR: " + delete_pokemon_id);
          if (this.pokemon[i].trained_pokemon_id === Number(delete_pokemon_id)) {
            index = i;
            break;
          }
        }
        this.$data.pokemon.splice(index, 1);
        console.log(this.$data.pokemon);
        this.forceRerender();
      });
    },
    deleteForm(trained_pokmeon_id, trainer_id) {
      console.log(trained_pokmeon_id);
      console.log(trainer_id);
      const delete_id_field = document.getElementById("delete-pokemon-id");
      const trainer_id_field = document.getElementById("trainer-id");
      delete_id_field.value = trained_pokmeon_id;
      trainer_id_field.value = trainer_id;
    },
    editForm(trained_pokemon_id) {
      console.log(trained_pokemon_id);
      let editedPokemon = this.pokemon.find((pokemon) => {
        return pokemon.trained_pokemon_id === trained_pokemon_id;
      });
      const pokemon_name_field = document.getElementById("pokemon-name");
      const pokemon_version_field = document.getElementById("version-name");
      const nickname_field = document.getElementById("nickname");
      const level_field = document.getElementById("level");
      const update_pokemon_id = document.getElementById("update-pokemon-id");
      const update_trainer_id = document.getElementById("update-trainer-id");
      console.log(editedPokemon);
      pokemon_name_field.value = editedPokemon.name;
      pokemon_version_field.value = editedPokemon.version;
      nickname_field.value = editedPokemon.nickname;
      level_field.value = editedPokemon.level;
      update_pokemon_id.value = editedPokemon.trained_pokemon_id;
      update_trainer_id.value = editedPokemon.trainer_id;
    },
    toggleData(show) {
      let opacity;
      if (show) {
        opacity = 1;
      } else {
        // eslint-disable-next-line no-unused-vars
        opacity = 0;
      }
    },
  },
  mounted() {
    console.log("mounted");
    let pane = this.$refs.pane;
    pane.style.opacity = 1;

    this.name = this.$props.trainerData.name;
    this.gender = this.$props.trainerData.gender;
    this.pokemon = this.$props.trainerData.pokemon;
    this.trainer_id = this.$props.trainerData.trainer_id;
    this.toggleData(true);
    gsap.fromTo(pane, { top: "50vh" }, { top: "10vh", bottom: "10vh", duration: 1, ease: "expo" });
  },
  updated() {
    this.name = this.$props.trainerData.name;
    this.gender = this.$props.trainerData.gender;
    this.pokemon = this.$props.trainerData.pokemon;
    this.toggleData(true);
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
