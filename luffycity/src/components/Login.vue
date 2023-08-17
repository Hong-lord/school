<template>
    <div class="login">
        <div class="box">
            <i class="el-icon-close" @click="close_login"></i>
            <div class="content">
                <div class="nav">
                    <span :class="{active: login_method === 'is_pwd'}"
                          @click="change_login_method('is_pwd')">密码登录</span>
                    <span :class="{active: login_method === 'is_sms'}"
                          @click="change_login_method('is_sms')">短信登录</span>
                </div>

                <el-form v-if="login_method === 'is_pwd'">
                    <el-input
                            placeholder="用户名/手机号/邮箱"
                            prefix-icon="el-icon-user"
                            v-model="username"
                            clearable>
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-button type="primary" @click="login">登录</el-button>
                </el-form>

                <el-form v-if="login_method === 'is_sms'">
                    <el-input
                            placeholder="手机号"
                            prefix-icon="el-icon-phone-outline"
                            v-model="mobile"
                            clearable
                            @blur="check_mobile">
                    </el-input>
                    <el-input
                            placeholder="验证码"
                            prefix-icon="el-icon-chat-line-round"
                            v-model="sms"
                            clearable>
                        <template slot="append">
                            <span class="sms" @click="send_sms">{{ sms_interval }}</span>
                        </template>
                    </el-input>
                    <el-button @click="mobile_login" type="primary">登录</el-button>
                </el-form>

                <div class="foot">
                    <span @click="go_register">立即注册</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
                mobile: '',
                sms: '',  // 验证码
                login_method: 'is_pwd',
                sms_interval: '获取验证码',
                is_send: false,
            }
        },
        methods: {
            close_login() {
                this.$emit('close')
            },
            go_register() {
                this.$emit('go')
            },
            change_login_method(method) {
                this.login_method = method;
            },
            check_mobile() {
                if (!this.mobile) return;
                // js正则：/正则语法/
                // '字符串'.match(/正则语法/)
                if (!this.mobile.match(/^1[3-9][0-9]{9}$/)) {
                    this.$message({
                        message: '手机号有误',
                        type: 'warning',
                        duration: 1000,
                        onClose: () => {
                            this.mobile = '';
                        }
                    });
                    return false;
                }
                // 后台校验手机号是否已存在
                this.$axios({
                    url: this.$settings.base_url + '/user/mobile/',
                    method: 'post',
                    data: {
                        mobile: this.mobile
                    }
                }).then(response => {
                    let result = response.data.result;
                    if (result) {
                        this.$message({
                            message: '账号正常',
                            type: 'success',
                            duration: 1000,
                        });
                        // 发生验证码按钮才可以被点击
                        this.is_send = true;
                    } else {
                        this.$message({
                            message: '账号不存在',
                            type: 'warning',
                            duration: 1000,
                            onClose: () => {
                                this.mobile = '';
                            }
                        })
                    }
                }).catch(() => {
                });
            },
            send_sms() {
                // this.is_send必须允许发生验证码，才可以往下执行逻辑
                if (!this.is_send) return;
                // 按钮点一次立即禁用
                this.is_send = false;

                let sms_interval_time = 60;
                this.sms_interval = "发送中...";

                // 定时器: setInterval(fn, time, args)

                // 往后台发送验证码
                this.$axios({
                    url: this.$settings.base_url + '/user/sms/',
                    method: 'get',
                    params: {
                        mobile: this.mobile
                    }
                }).then(response => {
                    let result = response.data.result;
                    if (result) { // 发送成功
                        let timer = setInterval(() => {
                            if (sms_interval_time <= 1) {
                                clearInterval(timer);
                                this.sms_interval = "获取验证码";
                                this.is_send = true; // 重新回复点击发送功能的条件
                            } else {
                                sms_interval_time -= 1;
                                this.sms_interval = `${sms_interval_time}秒后再发`;
                            }
                        }, 1000);
                    } else {  // 发送失败
                        this.sms_interval = "重新获取";
                        this.is_send = true;
                        this.$message({
                            message: '短信发送失败',
                            type: 'warning',
                            duration: 3000
                        });
                    }
                }).catch(() => {
                    this.sms_interval = "频率过快";
                    this.is_send = true;
                })


            },
            login() {
                if (!(this.username && this.password)) {
                    this.$message({
                        message: '请填好账号密码',
                        type: 'warning',
                        duration: 1500
                    });
                    return false  // 直接结束逻辑
                }

                this.$axios({
                    url: this.$settings.base_url + '/user/login/',
                    method: 'post',
                    data: {
                        username: this.username,
                        password: this.password,
                    }
                }).then(response => {
                    let username = response.data.result.username;
                    let token = response.data.result.token;
                    let user_id = response.data.result.id;
                    this.$cookies.set('username', username, '7d');
                    this.$cookies.set('token', token, '7d');
                    this.$cookies.set('user_id', user_id, '7d');
                    this.$emit('success', response.data.result);
                }).catch(error => {
                    console.log(error.response.data)
                })
            },
            mobile_login () {
                if (!(this.mobile && this.sms)) {
                    this.$message({
                        message: '请填好手机与验证码',
                        type: 'warning',
                        duration: 1500
                    });
                    return false  // 直接结束逻辑
                }

                this.$axios({
                    url: this.$settings.base_url + '/user/mobile/login/',
                    method: 'post',
                    data: {
                        mobile: this.mobile,
                        code: this.sms,
                    }
                }).then(response => {
                    let username = response.data.result.username;
                    let token = response.data.result.token;
                    let user_id = response.data.result.id;
                    this.$cookies.set('username', username, '7d');
                    this.$cookies.set('token', token, '7d');
                    this.$cookies.set('user_id', user_id, '7d');
                    this.$emit('success', response.data.result);
                }).catch(error => {
                    console.log(error.response.data)
                })
            }
        }
    }
</script>

<style scoped>
    .login {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 420px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 210px);
        left: calc(50vw - 200px);
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

    .el-icon-close:hover {
        color: darkred;
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin: 0 20px 0 35px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 40px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .sms {
        color: orange;
        cursor: pointer;
        display: inline-block;
        width: 70px;
        text-align: center;
        user-select: none;
    }
</style>