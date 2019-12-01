import Vue from 'vue'
import Vuex from 'vuex'
import axios from './configaxios.js'

Vue.use(Vuex)

export default new Vuex.Store({

    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        campaign: 5,
        user: 12
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading'
          },
          auth_success(state, token) {
            state.status = 'success'
            state.token = token
          },
          auth_error(state) {
            state.status = 'error'
          },
          logout(state) {
            state.status = ''
            state.token = ''
          },
          saveInfo(state, {user,campaign}){
            state.campaign = campaign
            state.user = user
          }
    },
    actions: {

        login({ commit }, data) {
            return new Promise((resolve, reject) => {
              commit('auth_request')
              axios.post('/login/', data)
                .then(resp => {
                  const token = resp.data.access
                  localStorage.setItem('token', token)
                  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
                  commit('auth_success', token)
                  resolve(resp)
                })
                .catch(err => {
                  commit('auth_error')
                  localStorage.removeItem('token')
                  reject(err.response)
                })
            })
          }, 

          register({ commit }, data) {
            return new Promise((resolve, reject) => {
              commit('auth_request')
              axios.post('/register/', data)
                .then(resp => {
                 /* const token = resp.data.token
                  localStorage.setItem('token', token)
                  axios.defaults.headers.common['Authorization'] = token
                  commit('auth_success', token)*/
                  resolve(resp)
                })
                .catch(err => {
                  commit('auth_error', err)
                  localStorage.removeItem('token')
                  reject(err.response)
                })
            })
          }, 

          logout({commit}){
            return new Promise((resolve, reject) => {
              commit('logout')
              localStorage.removeItem('token')
              delete axios.defaults.headers.common['Authorization']
              resolve()
            })
          },
          saveNarrative({commit}, data){
            const campaign = data.campaign
            const user = data.user
            commit('saveInfo', {user,campaign})
          }

      },
    
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status
      }
    })