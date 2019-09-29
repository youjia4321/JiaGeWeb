import Header from "@/components/JiageHeader"
import Footer from "@/components/JiageFooter"
const Index = () => import("@/views/index/JiageIndex")
const Cate = () => import("@/views/index/JiageCateClick")
const Login = () => import("@/views/login/JiageLogin")
const Register = () => import("@/views/register/JiageRegister")

const Profile = () => import("@/views/profile/JiageProfile")
const mineBlog = () => import("@/views/profile/JiageMineBlog")
const mineCollect = () => import("@/views/profile/JiageCollect")
const Center = () => import("@/views/profile/JiageCenter")

const addBlog = () => import("@/views/addblog/JiageAddBlog")
const editBlog = () => import("@/views/addblog/JiageEditBlog")
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
    },
    {
        path: "/account/mineblog",
        name: "Mineblog",
        components: {
            default: mineBlog,
            header: Header,
            footer: Footer
        }
    },
    {
        path: "/account/collect",
        name: "Collect",
        components: {
            default: mineCollect,
            header: Header,
            footer: Footer
        }
    },
    {
        path: "/account/center",
        name: "Center",
        components: {
            default: Center,
            header: Header,
            footer: Footer
        }
    },
    {
        path: "/account/edit/blog",
        name: "Editblog",
        components: {
            default: editBlog,
            footer: Footer,
            header: Header
        }

    },
    {
        path: '/cate/list',
        name: 'Cate',
        components: {
            default: Cate,
            header: Header,
            footer: Footer
        }
    }
]