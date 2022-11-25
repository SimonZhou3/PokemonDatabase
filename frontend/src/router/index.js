import {createRouter, createWebHistory} from 'vue-router'

import searchPokemon from '../views/pokemonSearch'
import searchTrainer from '../views/trainerSearch'
import trainerCount from '../views/trainerCount'

const routes = [
    {
        path: "/",
        name: 'Pokemon',
        component: searchPokemon
    },
    {
        path: "/trainer",
        name: 'trainer',
        component: searchTrainer
    },
    {
        path: "/trainer/leaderboard",
        name: 'board',
        component: trainerCount
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
})



export default router