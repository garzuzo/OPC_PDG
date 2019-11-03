import axios from './configaxios.js'

export default {
    
    /*
    CAMPAIGNS
    */
    getActiveCampaigns() {
        return new Promise((resolve, reject) => {
            axios.get('/activecampaigns/')
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting active campaigns', err);
                })
        });
    },
    getNotActiveCampaigns() {
        return new Promise((resolve, reject) => {
            axios.get('/notactivecampaigns/')
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting not active campaigns', err);
                })
        });
    },

    getPeopleByCampaignAndComuna(data){
        return new Promise((resolve, reject) => {
            axios.get(`/women_men/?id=${data[0]}&comuna=${data[1]}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting people', err);
                })
        });
    },

    getRangesOfAgeByCampaignAndComuna(data){
        return new Promise((resolve, reject) => {
            axios.get(`/ages/?id=${data[0]}&comuna=${data[1]}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting ranges of age', err);
                })
        });
    },

    getNarratives(idCampaign){
        return new Promise((resolve, reject) => {
            axios.get(`/narratives/?id=${idCampaign}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting narratives', err);
                })
        });
    },
    getKeywords(idCampaign){
        return new Promise((resolve, reject) => {
            axios.get(`/keywords/?id=${idCampaign}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting keywords', err);
                })
        });
    },
    /*
    EDUCATION
    */
    getLevelsEducation() {
        return new Promise((resolve, reject) => {
            axios.get('/levelseducation/')
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting levels of education', err);
                })
        });
    },

    getAchievedLevel(levelEducation) {
        return new Promise((resolve, reject) => {
            axios.get(`/levelineducation/?name=${levelEducation}`)
                .then((response) => {
                    resolve(response.data);
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
   getZones(){
        return new Promise((resolve, reject) => {
            axios.get(`/zones/`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting zones', err);
            })
        });
   },
   getStates(country) {
        return new Promise((resolve, reject) => {
            axios.get(`/states/?country=${country}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    getCities(state) {
        return new Promise((resolve, reject) => {
            axios.get(`/cities/?state=${state}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    getCorregimientosComunas(data) {
        return new Promise((resolve, reject) => {
            axios.get(`/corregimientos_comunas/?city=${data[0]}&zone=${data[1]}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    getNeighborhoodsVeredas(data) {
        return new Promise((resolve, reject) => {
            axios.get(`/veredas_neighborhoods/?city=${data[0]}&zone=${data[1]}&comuna_corregimiento=${data[2]}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    },
    saveData(data){
        return new Promise((resolve, reject) => {
            axios.post(`/saveall/`, data)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting the achieved level', err);
            })
        });
    }
}