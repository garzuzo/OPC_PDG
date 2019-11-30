import axios from 'axios'

export default axios.create({
    baseURL: 'http://pi2sis.icesi.edu.co/opcapi', 
    headers: {
     'X-Requested-With': 'XMLHttpRequest',
     //'Content-Type': 'application/x-www-form-urlencoded', 
    // 'Access-Control-Allow-Origin' : '*',
    // 'Access-Control-Allow-Headers' : 'Access-Control-Allow-Headers, Access-Control-Allow-Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers',
     //'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,OPTIONS'
    }
})

/*const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = 'Bearer '+ token 
}*/
