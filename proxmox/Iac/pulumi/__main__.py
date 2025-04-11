import pulumi_proxmoxve as proxmox
import pulumi

virtual_machine = proxmox.vm.VirtualMachine(
    resource_name="vm",
    node_name="medusa-sn1",
    agent=proxmox.vm.VirtualMachineAgentArgs(
        enabled=True, # toggles checking for ip addresses through qemu-guest-agent
        trim=True,
        type="virtio"
    ),
    bios="seabios",
    cpu=proxmox.vm.VirtualMachineCpuArgs(
        cores=4,
        sockets=1,
        type="host"
    ),
    disks=[
        proxmox.vm.VirtualMachineDiskArgs(
            interface="scsi0",
            datastore_id="local-lvm",
            size=32,
            file_format="raw"
        )
    ],
    cdrom={
        "enabled": True,
        "file_id":"local:iso/1.19-metal-amd64.iso",
        "interface":"ide0"

    },
   
    memory=proxmox.vm.VirtualMachineMemoryArgs(
        dedicated=2048
    ),
    name="proxmox-vm",
    network_devices=[
        proxmox.vm.VirtualMachineNetworkDeviceArgs(
            bridge="vmbr0",
            model="virtio"
        )
    ],
    on_boot=True,
    boot_orders=["scsi0","ide0"],
    started=True,
    operating_system=proxmox.vm.VirtualMachineOperatingSystemArgs(type="l26"),
)

virtual_machine1 = proxmox.vm.VirtualMachine(
    resource_name="gloo-ee-flux",
    node_name="medusa-sn1",
    agent=proxmox.vm.VirtualMachineAgentArgs(
        enabled=True, # toggles checking for ip addresses through qemu-guest-agent
        trim=True,
        type="virtio"
    ),
    bios="seabios",
    cpu=proxmox.vm.VirtualMachineCpuArgs(
        cores=4,
        sockets=1,
        type="host"
    ),
    disks=[
        proxmox.vm.VirtualMachineDiskArgs(
            interface="scsi0",
            datastore_id="local-lvm",
            size=32,
            file_format="raw"
        )
    ],
    cdrom={
        "enabled": True,
        "file_id":"local:iso/1.19-metal-amd64.iso",
        "interface":"ide0"

    },
    memory=proxmox.vm.VirtualMachineMemoryArgs(
        dedicated=4048
    ),
    name="gloo-ee-flux",
    network_devices=[
        proxmox.vm.VirtualMachineNetworkDeviceArgs(
            bridge="vmbr0",
            model="virtio"
        )
    ],
    on_boot=True,
    boot_orders=["scsi0","ide0"],
    started=True,
    operating_system=proxmox.vm.VirtualMachineOperatingSystemArgs(type="l26"),
)
