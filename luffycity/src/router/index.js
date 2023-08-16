import Vue from 'vue'
import VueRouter from 'vue-router'
import ActualCourse from '../views/ActualCourse.vue'
import FreeCoursr from '../views/FreeCourse.vue'
import LightCourse from '../views/LightCourse.vue'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/actual-course',
        name: 'ActualCourse',
        component: ActualCourse
    },
    {
        path: '/free-course',
        name: 'FreeCourse',
        component: FreeCoursr
    },
    {
        path: '/light-course',
        name: 'LightCourse',
        component: LightCourse
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
