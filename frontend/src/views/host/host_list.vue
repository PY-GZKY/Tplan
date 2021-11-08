<template>
  <div class="app-container">
    <div class="filter-container">
      <el-row :gutter="20">
        <el-col :span="20" :xs="24">
          <el-form :inline="true" label-position="right">
            <el-form-item size="small" label="状态">
              <el-select placeholder="全部" v-model="listQuery.status">
                <el-option label="全部" value="" key="" />
                <el-option value="1" label="在线" />
                <el-option value="-1" label="离线" />
                <el-option value="0" label="未知" />
              </el-select>
            </el-form-item>

            <el-button
              v-waves
              size="small"
              type="success"
              icon="el-icon-plus"
              @click="handleCreate"
              >创建节点</el-button
            >
          </el-form>
        </el-col>
      </el-row>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column align="center" label="服务器名称" width="160">
        <template slot-scope="{ row }">
          <span>{{ row.host_name }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="IP地址" width="150">
        <template slot-scope="{ row }">
          <span>{{ row.ip }}</span>
        </template>
      </el-table-column>

      <el-table-column width="110px" align="center" label="端口">
        <template slot-scope="{ row }">
          <span>{{ row.port }}</span>
        </template>
      </el-table-column>

      <el-table-column width="160px" align="center" label="用户名">
        <template slot-scope="{ row }">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>

      <el-table-column label="类型" width="140" align="center">
        <template slot-scope="{ row }">
          <div>
            <el-button
              v-if="row.host_type == '主节点'"
              style="font-weight: bold"
              type="primary"
              plain
              size="mini"
            >
              <i style="font-weight: bold" size="mini"></i>
              {{ row.host_type }}
            </el-button>
            <el-button
              v-else
              style="font-weight: bold"
              type="warning"
              plain
              size="mini"
            >
              <i style="font-weight: bold" size="mini"></i>
              {{ row.host_type }}
            </el-button>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="节点状态" width="140" align="center">
        <template slot-scope="{ row }">
          <div>
            <el-button
              v-if="row.host_status == 1"
              style="font-weight: bold"
              type="success"
              plain
              size="mini"
              ><i size="mini" class="el-icon-loading"></i>
              正在运行
            </el-button>
            <el-button
              v-else-if="row.host_status == 0"
              style="font-weight: bold"
              type="primary"
              plain
              size="mini"
            >
              <i style="font-weight: bold" size="mini"></i>
              未知
            </el-button>
            <el-button
              v-else
              style="font-weight: bold"
              type="info"
              plain
              size="mini"
            >
              <i style="font-weight: bold" size="mini"></i>
              离线
            </el-button>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="免密登陆" width="120" align="center">
        <template slot-scope="{ row }">
          <!-- <el-button v-if="row.is_verify" plain type="success">已开启</el-button> -->
          <el-switch
            v-model="row.is_verify"
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
          <!-- <div>
            <el-tooltip
              v-else
              class="item"
              effect="dark"
              content="请前往授权"
              placement="top-start"
            >
              <el-button type="info" plain>未授权</el-button>
            </el-tooltip>
          </div> -->
        </template>
      </el-table-column>

      <el-table-column label="描述" width="290" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.desc }}</span>
        </template></el-table-column
      >

      <!-- <el-table-column label="更新时间" width="200" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.update_time }}</span>
        </template></el-table-column
      > -->

      <el-table-column label="操作" align="center" fixed="right" width="560">
        <template slot-scope="{ row }">
          <div>
            <el-tooltip
              class="item"
              effect="dark"
              content="详细信息"
              placement="top-start"
            >
              <el-button
                type="primary"
                icon="el-icon-search"
                size="mini"
                @click="handleDetail(row)"
                >查看</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="修改连接"
              placement="top-start"
            >
              <el-button
                type="info"
                icon="el-icon-edit"
                size="mini"
                @click="handleUpdate(row)"
                >编辑</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="安装依赖包"
              placement="top-start"
            >
              <el-button
                type=""
                icon="el-icon-bottom"
                size="mini"
                @click="handleDeploy(row)"
                >安装</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="测试连接"
              placement="top-start"
            >
              <el-button
                type="success"
                icon="el-icon-s-promotion"
                size="mini"
                @click="handleTest(row)"
                >测试</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="远程编码"
              placement="top-start"
            >
              <el-button
                type="warning"
                icon="el-icon-s-promotion"
                size="mini"
                @click="handleCodeServer(row)"
                >远程编码</el-button
              >
            </el-tooltip>

            <el-tooltip
              class="item"
              effect="dark"
              content="删除节点"
              placement="top-start"
            >
              <el-button
                type="danger"
                icon="el-icon-delete"
                size="mini"
                @click="handleDelete(row)"
                >删除</el-button
              >
            </el-tooltip>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total > 0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getList"
    />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form
        ref="dataForm"
        :rules="rules"
        :model="temp"
        label-position="left"
        label-width="85px"
        style="width: 600px; margin-left: 25px"
      >
        <el-form-item label="主机名称" prop="host_name">
          <el-input v-model="temp.host_name" placeholder="主机名称"></el-input>
        </el-form-item>
        <el-form-item label="类型" prop="host_type">
          <el-select v-model="temp.host_type" placeholder="从节点">
            <el-option
              key="主节点"
              label="主节点(设定该节点为主节点)"
              :disabled="true"
              value="主节点"
            ></el-option>
            <el-option
              key="工作节点"
              label="工作节点"
              value="工作节点"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="IP" prop="ip">
          <el-input v-model="temp.ip" placeholder="IP"></el-input>
        </el-form-item>
        <el-form-item label="端口" prop="port">
          <el-input v-model="temp.port" placeholder="22"></el-input>
        </el-form-item>

        <el-form-item label="用户名" prop="username">
          <el-input v-model="temp.username" placeholder="用户名"></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="password">
          <el-input
            v-model="temp.password"
            show-password
            placeholder="密码"
          ></el-input>
        </el-form-item>

        <el-form-item label="描述" prop="desc">
          <el-input v-model="temp.desc" placeholder="填写描述"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false"> 取消 </el-button>
        <el-button
          type="primary"
          @click="dialogStatus === 'create' ? createData() : updateData()"
        >
          确认
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {
  host_list,
  create_host,
  update_host,
  delete_host,
  test_host,
} from "@/api/host";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination
export default {
  name: "H",
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      textMap: {
        update: "Edit",
        create: "Create",
      },
      listQuery: {
        page: 1,
        limit: 15,
        status: null,
      },
      temp: {},
      test_temp: {},
      nowRow: "",
      dialogFormVisible: false,
      dialogStatus: "",
      showViewer: false,
      rules: {
        host_name: [
          {
            required: true,
            message: "host_name is required",
            trigger: "change",
          },
        ],
        host_type: [
          {
            required: true,
            message: "host_type is required",
            trigger: "change",
          },
        ],
        ip: [
          {
            required: true,
            message: "ip is required",
            trigger: "change",
          },
        ],
        port: [
          { required: true, message: "port is required", trigger: "change" },
        ],
        username: [
          {
            required: true,
          },
        ],
        password: [
          {
            required: true,
            message: "password is required",
            trigger: "change",
          },
        ],
        desc: [
          { required: true, message: "desc is required", trigger: "change" },
        ],
      },
      downloadLoading: false,
    };
  },

  created() {
    this.getList();
  },
  methods: {
    getList() {
      this.listLoading = true;
      host_list(this.listQuery).then((response) => {
        this.list = response.data.items;
        this.total = response.data.total;
        setTimeout(() => {
          this.listLoading = false;
        }, 1.5 * 1000);
      });
    },

    resetTemp() {
      this.temp = {
        host_name: "",
        host_type: "",
        ip: "",
        port: "",
        username: "",
        password: "",
        desc: "描述",
        update_time: this.dayjs().format("YYYY-MM-DD HH:mm:ss"),
      };
    },
    handleCreate() {
      this.resetTemp();
      this.dialogStatus = "create";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    createData() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          console.log("this.temp:", this.temp);
          create_host(this.temp).then(() => {
            this.dialogFormVisible = false;
            this.$notify({
              title: "Success",
              message: "创建成功",
              type: "success",
              duration: 2000,
            });
            this.getList();
          });
        }
      });
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row); // copy obj
      this.dialogStatus = "update";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    updateData() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp);
          // tempData.timestamp = +new Date(tempData.timestamp); // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          update_host(tempData).then(() => {
            this.dialogFormVisible = false;
            this.$notify({
              title: "Success",
              message: "更新成功",
              type: "success",
              duration: 2000,
            });
            this.getList();
          });
        }
      });
    },

    handleDelete(row) {
      this.$confirm("确认删除该项?", "警告", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(
        () =>
          // delete_host({ uuid: row.uuid }).then(() => {
          this.$notify({
            title: "Warning",
            message: "演示环境看看得了",
            type: "warning",
            duration: 2000,
          })
        //   this.getList();
        // })
      );
    },

    handleTest(row) {
      this.test_temp.uuid = row.uuid;
      this.test_temp.ip = row.ip;
      test_host(this.test_temp)
        .then((res) => {
          if (res.code == 20000) {
            this.$notify({
              title: res.data.ip + "(连接成功)",
              message: res.data.uname + "\n" + new Date().toLocaleTimeString(),
              type: "success",
              duration: 0,
            });
            this.getList();
          }
        })
        .catch(() => {
          this.$notify({
            title: this.test_temp.ip + "(连接失败)",
            message: "请检查配置项 " + new Date().toLocaleTimeString(),
            type: "error",
            duration: 0,
          });
        });
    },

    handleDetail(row) {
      const self = this;
      self.$router.push(`/host_detail/${row.uuid}`);
    },

    handleDeploy(row) {
      const self = this;
      self.$router.push(`/host_deploy/${row.uuid}`);
    },

    handleCodeServer(row) {
      this.$notify({
        title: "未开放的功能",
        message: "可以期待一下 ",
        type: "warning",
        duration: 0,
      });
      // const self = this;
      // self.$router.push(`/code_server/index`);
    },
  },
};
</script>
