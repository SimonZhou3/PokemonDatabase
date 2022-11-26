<template>
  <div>
    <button v-if="!showImage" class="btn btn-outline-info" data-bs-toggle="modal" data-bs-target="#addTrainerModal">
      <i class="bi bi-plus-square-fill">
        Add Trainer
      </i>
    </button>
    <button v-if="!showImage" class="btn btn-outline-danger spread-button" data-bs-toggle="modal" data-bs-target="#deleteTrainerModal">
      <i class="bi bi-x">
        Delete Trainer
      </i>
    </button>
    <div class="barContainer" ref="barContainer" @click="this.reset">
      <input
          class="search"
          ref="search"
          type="text"
          v-model="this.query"
          placeholder="Search Trainer"
          v-if="!loading"
      />
      <div class="pokeball" ref="pokeball" v-show="this.loading">
        <div class="ballTop" ref="ballTop"></div>
        <div class="ballMid" ref="ballMid"></div>
        <div class="ballCenter" id="outer" ref="ballCenterOuter">
          <div class="ballCenter" id="inner" ref="ballCenterInner"></div>
        </div>
        <div
            v-if="showImage"
            class="image"
            ref="sprite"
            v-bind:style="{ backgroundImage: `url(${this.$props.sprite})` }"
        >
        </div>
        <div class="ballBottom" ref="ballBot"></div>
      </div>
      <div
          class="searchResults"
          ref="searchResults"
          v-if="this.query.length > 0"
      >
        <div v-for="trainer of findTrainers" :key="trainer">
          <TrainerEntry
              :trainer="trainer"
              v-show="this.query.length > 1"
              @querying="onQuery"
          />
        </div>
      </div>
    </div>
  </div>

<!-- Add Trainer Modal -->
  <div class="modal fade" id="addTrainerModal" tabindex="-1" aria-labelledby="addTrainerModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="editModalLabel">Add Trainer</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label">Name</label>
              <input class="form-control" id="trainer-name" />
            </div>
            <div class="mb-3">
              <label class="form-label">Gender</label>
              <select class="form-control" id="gender">
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-primary" v-on:click="addTrainer" data-bs-dismiss="modal">
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>
<!--  Delete Trainer Modal-->
  <div class="modal fade" id="deleteTrainerModal" tabindex="-1" aria-labelledby="addTrainerModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="deleteTrainer">Delete a Trainer</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label">Trainer</label>
              <select class="form-control" id="trainer-id">
                <option
                    v-for="trainer in this.$props.trainerList"
                    v-bind:key="trainer.trainer_id"
                    :value="trainer.trainer_id"
                >
                  {{trainer.trainer_id}} -- {{trainer.name }}
                </option>
              </select>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-outline-danger" v-on:click="deleteTrainerFromLocal" data-bs-dismiss="modal">
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import TrainerEntry from './trainerEntry';
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import {nextTick} from "vue";

export default {
  name: "SearchBar",
  components: {
    TrainerEntry,
  },
  props: ["trainerList", "received", "sprite","queryTrainer","deleteTrainer"],
  data() {
    return {
      query: "",
      loading: false,
      loaded : false,
      showImage: false,
      trainerSprite: this.$props.sprite,
    };
  },
  computed: {
    findTrainers() {
      let filteredList = [];
      console.log(this.$props.trainerList)
      for (let trainer of this.$props.trainerList) {
        if (trainer.name.toLowerCase().startsWith(this.query.toLowerCase())) {
          filteredList.push(trainer);
        }
      }
      return filteredList;
    },
  },
  methods: {

    reset() {
      if (this.loaded) {
        console.log("resetting to original state");
        let sprite = this.$refs.sprite;
        gsap.to(sprite, { scale: 0, duration: 0.5, ease: "back.in" });
        this.$emit("reset");
        let barContainer = this.$refs.barContainer;
        barContainer.style.transformOrigin = "center";
        gsap.to(barContainer, { top: "45vh", duration: 1, ease: "expo" });
        gsap.to(barContainer, {
          height: "10vh",
          duration: 0.5,
          ease: "expo",
          delay: 0.3,
        });
        gsap.to(barContainer, {
          width: "65vw",
          duration: 0.5,
          ease: "expo",
          delay: 0.5,
          onComplete: () => {
            this.loading = false;
            this.loaded = false;
            this.showImage = false;
            this.$emit("resetComplete")
          },
        });

      }
    },

    async forceRerender() {
      this.renderComponent = false;
      await nextTick();
      this.renderComponent = true;
      console.log("rerendered...");
    },

    async deleteTrainerFromLocal() {
      console.log('enter delete Trainer')
      const trainerID = document.getElementById('trainer-id').value;
      let t = await this.$props.deleteTrainer(trainerID);
      console.log(t)
      let index = 100000;
      for (let i = 0; i < this.$props.trainerList.length; i++) {
        if (this.$props.trainerList[i].trainer_id === Number(trainerID)) {
          index = i
          break;
        }
      }
      console.log("INDEX NUMBER: " + index)
      this.$props.trainerList.splice(index,1);
      this.forceRerender()
    },

    async addTrainer() {
      console.log('enter add Trainer')
      const trainerName = document.getElementById('trainer-name').value;
      const gender = document.getElementById('gender').value;
      let t = await this.$props.queryTrainer(trainerName, gender);
      console.log(t)
      this.$props.trainerList.push(t)
      this.forceRerender()
    },

    toggleSprite() {
      let sprite = this.$refs.sprite;
      console.log(sprite)
      gsap.fromTo(sprite , { y: 20 }, { y: 0, duration: 0.5, ease: "expo" });
    },

    showTrainer() {
      let barContainer = this.$refs.barContainer;
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
          this.showImage = true;
          this.loaded = true;
          this.toggleSprite;
        },
      });

      gsap.to(ballBot, { scale: 10, duration: 0.2, delay: 0.4 });

      gsap.to(barContainer, {
        top: "5vh",
        duration: 1,
        ease: "expo",
        delay: 0.5,
      });
    },
    stopAnimation() {
      if (this.$props.received) {
        console.log("stopping animation");
        let all = gsap.exportRoot();
        gsap.to(all, { timeScale: 0 });
        let barContainer = this.$refs.barContainer;
        gsap.to(barContainer, {
          rotate: 0,
          duration: 0.5,
          ease: "elastic",
          onComplete: this.showTrainer,
        });
      }
    },
    waitForResults() {
      console.log("waiting for query to complete");
      // this.$refs.barContainer.style.backgroundColor = "#00000000";
      let barContainer = this.$refs.barContainer;
      barContainer.style.transformOrigin = "bottom";
      gsap.to(barContainer, { rotation: 20, duration: 0.2, ease: "expo" });
      gsap.to(barContainer, {
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
    onQuery(trainer_id) {
      console.log("querying");
      this.loading = true;
      this.query = "";
      this.loadAnimation();
      this.$emit("querying", trainer_id);
    },
    resize(height) {
      if (!this.loading) {
        let container = this.$refs.barContainer;
        gsap.to(container, { height: height, duration: 0.2, ease: "expo" });
      }
    },
  },
  mounted() {
    console.log('PROPS:')
    console.log(this.$props.trainerList)
  },
  updated() {
    if (this.query.length > 1) {
      //limit height of container
      let requiredHeight = this.findTrainers.length * 6 + 11;
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
  overflow: hidden;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}
.barContainer:hover {
  /* background-color: #cf4444; */
  cursor: pointer;
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
  transform: translateY(-0.5%);
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
  position: absolute;
  background-color: #000000;
  height: 30%;
  width: 30%;
  border-radius: 50%;
  left: 35%;
  display: inline-block;
  top: 35%;
  transform-origin: center;
}
.ballCenter#inner {
  position: absolute;
  background-color: #ffffff;
  height: 60%;
  width: 60%;
  left: 20.5%;
  display: inline-block;
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
.image {
  /* border: 1px solid red; */
  /* border-radius: 2.5vh; */
  position: relative;

  left: 0vh;
  top: -12vh;
  height: 100%;
  width: 100%;
  display: inline-block;
  z-index: 100;
  opacity: 1;
  transition: opacity 1s;
  /* background-color: rgb(17, 71, 117); */
  background-size: cover;
}
.debug {
  position: absolute;
  left: 0%;
  top: 0%;
}

.spread-button {
  margin-left: 2rem;
}
</style>