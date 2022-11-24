import {createRouter, createWebHistory} from 'vue-router'

import searchPokemon from '../views/pokemonSearch'

const routes = [
    {
        path: "/",
        name: 'Pokemon',
        component: searchPokemon
    },
]


const router = createRouter({
    history: createWebHistory(),
    routes,
})



export default router