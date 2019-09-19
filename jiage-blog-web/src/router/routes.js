import Header from "@/components/JiageHeader"
const Index = () => import("@/views/JiageIndex")
const Login = () => import("@/views/JiageLogin")
const Register = () => import("@/views/JiageRegister")

export default [
    {
        path: "/",
        redirect: '/index',
    },
    {
        path: '/index',
        name: 'index',
        components: {
            default: Index,
            header: Header
        }
    },
    {
        path: '/account/login',
        name: "login",
        components: {
            default: Login
        }
    },
    {
        path: '/account/register',
        name: "register",
        components: {
            default: Register
        }
    }
]