import Header from "@/components/JiageHeader"
const Index = () => import("@/views/JiageIndex")
const Login = () => import("@/views/JiageLogin")

export default [
    {
        path: '/',
        name: 'index',
        components: {
            default: Index,
            header: Header
        }
    },
    {
        path: '/login',
        name: "login",
        components: {
            default: Login
        }
    }
]