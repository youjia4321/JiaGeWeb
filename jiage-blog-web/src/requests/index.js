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

// 用户注册
export const userRegister = (email, username, password, headers) => {
    return ajax({
        url: '/api/userRegister',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'email': email, 'username': username, 'password': password }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}


// 发布博客
export const addBlog = (title, author, content, category, tag, headers) => {
    return ajax({
        url: '/api/addBlog',
        method: 'post',
        responseType: 'json',
        data: qs.stringify({ 'title': title, 'author': author, 'content': content, 'category': category, 'tag': tag }),
        headers: {
            'X-CSRFToken': headers
        }
    })
}

// 博客列表
export const listOfBlog = () => {
    return ajax({
        url: '/api/listOfBlog',
        method: 'get',
        responseType: 'json'
    })
}

// 博客详情
export const blogDetails = (id) => {
    return ajax.get(`/api/blog/${id}`)
}