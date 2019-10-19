import axios from './configaxios.js'

export default {
    
    /*
    EDUCATION
    */
    getLevelsEducation() {
        return new Promise((resolve, reject) => {
            axios.get('/levelseducation/')
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error getting levels of education', err);
                })
        });
    },

    getAchievedLevel(levelEducation) {
        return new Promise((resolve, reject) => {
            axios.get(`/levelineducation?name=${levelEducation}/`)
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
                })
        });
    },

     /*
    PERSONAL
    */

   getGender() {
        return new Promise((resolve, reject) => {
            axios.get('/gender/')
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting genders', err);
            })
        });
    },

    /*
    TERRITORY
    */
   getStates(country) {
        return new Promise((resolve, reject) => {
            axios.get(`/states?country=${country}/`)
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    getCities(state) {
        return new Promise((resolve, reject) => {
            axios.get(`/cities?state=${state}/`)
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    getCorregimientosComunas(data) {
        return new Promise((resolve, reject) => {
            axios.get(`/corregimientos_comunas?city=${data[0]}&zone=${data[1]}/`)
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    getNeighborhoodsVeredas(data) {
        return new Promise((resolve, reject) => {
            axios.get(`/veredas_neighborhoods?city=${data[0]}&zone=${data[1]}/`)
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
}