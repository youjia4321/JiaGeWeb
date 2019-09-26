import Header from "@/components/JiageHeader"
import Footer from "@/components/JiageFooter"
const Index = () => import("@/views/index/JiageIndex")
const Login = () => import("@/views/login/JiageLogin")
const Register = () => import("@/views/register/JiageRegister")

const Profile = () => import("@/views/profile/JiageProfile")
const addBlog = () => import("@/views/addblog/JiageAddBlog")
const blogDetail = () => import("@/views/details/JiageDetails")

export default [
    {
        path: "/",
        redirect: '/index',
    },
    {
        path: '/index',
        name: 'Index',
        components: {
            default: Index,
            header: Header,
            footer: Footer
        }
    },
    {
        path: '/account/login',
        name: "Login",
        components: {
            default: Login
        }
    },
    {
        path: '/account/register',
        name: "Register",
        components: {
            default: Register
        }
    },
    {
        path: '/account/profile',
        name: 'Profile',
        components: {
            default: Profile,
            header: Header,
            footer: Footer,

        },
        meta: { requireAuth: true }
    },
    {
        path: "/account/add/blog",
        name: "Addblog",
        components: {
            default: addBlog,
            header: Header,
            footer: Footer
        },
        meta: { requireAuth: true }
    },
    {
        path: "/blog/details",
        name: "Details",
        components: {
            default: blogDetail,
            header: Header,
            footer: Footer
        }
    }
]