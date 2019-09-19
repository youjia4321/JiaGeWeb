import axios from 'axios'
import { LoadingBar } from 'iview';
import qs from 'qs'

const isDev = process.env.NODE_ENV === 'development'

const ajax = axios.create({
    baseURL: isDev ? "http://192.168.1.65:8000" : "http://192.168.1.65:8000"
})


// 拦截器
ajax.interceptors.request.use((config) => {
    LoadingBar.start();
    return config
})

ajax.interceptors.response.use((resp) => {
    if (resp.status === 200) {
        LoadingBar.finish();
        return resp.data
    }
})

// 用户登录
export const userLogin = (username, password, headers) => {
    return ajax({
        url: '/api/userLogin',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'username': username, 'password': password }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}