import axios from './configaxios.js'
import store from './store'
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

    getPeopleByCampaignAndTerritory(data){
        return new Promise((resolve, reject) => {
            axios.get(`/women_men/?id=${data.id}&${data.territory}=${data.idTerritory}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting people', err);
                })
        });
    },

    getRangesOfAgeByCampaignAndTerritory(data){
        return new Promise((resolve, reject) => {
            axios.get(`/ages/?id=${data.id}&${data.territory}=${data.idTerritory}`)
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting ranges of age', err);
                })
        });
    },

    getEducationByCampaignAndTerritory(data){
        return new Promise((resolve, reject) => {
            axios.get(`/educations/?id=${data.id}&${data.territory}=${data.idTerritory}`)
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
                    resolve(response);
                })
                .catch((err) => {
                    reject(err);
            })
        });
    },

    //PROFILE
    getCityPerson(){
        return new Promise((resolve, reject) => {
            axios.get('/city_person/', { headers: {"Authorization" : `Bearer ${store.state.token}`} })
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting city', err);
            })
        });
    },
    getRoleUser(){
        return new Promise((resolve, reject) => {
            axios.get('/role_user/', { headers: {"Authorization" : `Bearer ${store.state.token}`} })
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting role', err);
            })
        });
    },
    getProfileCampaigns(){
        return new Promise((resolve, reject) => {
            axios.get('/campaigns_person/', { headers: {"Authorization" : `Bearer ${store.state.token}`} })
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting profile campaigns', err);
            })
        });
    },
    getCreatedCampaigns(){
        return new Promise((resolve, reject) => {
            axios.get('/campaigns_created_person/', { headers: {"Authorization" : `Bearer ${store.state.token}`}})
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting created campaigns', err);
            })
        });
    },
    saveCampaign(data){
        return new Promise((resolve, reject) => {
            axios.post(`/campaign/`, data, { headers: {"Authorization" : `Bearer ${store.state.token}`}} )
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error creating a campaign',err);
            })
        });
    },
    editCampaign(data){
        return new Promise((resolve, reject) => {
            axios.put(`/campaign/`, data, { headers: {"Authorization" : `Bearer ${store.state.token}`}} )
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error editing a campaign',err);
            })
        });
    },
    saveNarrativeLoggedUser(data){
        return new Promise((resolve, reject) => {
            axios.post(`/save_info_ruser/`, data, { headers: {"Authorization" : `Bearer ${store.state.token}`}} )
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error saving narrative',err);
            })
        });
    },
    editProfile(data){
        return new Promise((resolve, reject) => {
            axios.put(`/person_data/`, data, { headers: {"Authorization" : `Bearer ${store.state.token}`}} )
                .then((response) => {
                    resolve(response);
                })
                .catch((err) => {
                    reject('Error editing profile',err);
            })
        });
    },
    getProfile(){
        return new Promise((resolve, reject) => {
            axios.get(`/person_data/`, { headers: {"Authorization" : `Bearer ${store.state.token}`}} )
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting profile',err);
            })
        });
    },
    getUserActiveCampaigns(){
        return new Promise((resolve, reject) => {
            axios.get(`/acampaigns_person_list/`, { headers: {"Authorization" : `Bearer ${store.state.token}`}} )
                .then((response) => {
                    resolve(response.data);
                })
                .catch((err) => {
                    reject('Error getting user active campaign',err);
            })
        });
    }
}