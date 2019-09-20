import Header from "@/components/JiageHeader"
import Footer from "@/components/JiageFooter"
const Index = () => import("@/views/JiageIndex")
const Login = () => import("@/views/JiageLogin")
const Register = () => import("@/views/JiageRegister")

const Profile = () => import("@/views/profile/JiageProfile")
const addBlog = () => import("@/views/addblog/JiageAddBlog")

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
            header: Header,
            footer: Footer
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
    },
    {
        path: '/account/index',
        name: 'profile',
        components: {
            default: Profile,
            header: Header,
            footer: Footer
        }
    },
    {
        path: "/add/blog",
        name: "add",
        components: {
            default: addBlog,
            header: Header,
            footer: Footer
        }
    }
]