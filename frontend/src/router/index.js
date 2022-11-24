import {createRouter, createWebHistory} from 'vue-router'

import searchPokemon from '../views/pokemonSearch'
import searchTrainer from '../views/trainerSearch'

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
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
})



export default router