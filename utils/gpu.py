"""
Copyright [2022] Victor C Hall

Licensed under the GNU Affero General Public License;
You may not use this code except in compliance with the License.
You may obtain a copy of the License at

    https://www.gnu.org/licenses/agpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from pynvml.smi import nvidia_smi
import torch

class GPU:
    def __init__(self, device: torch.device):
        self.nvsmi = nvidia_smi.getInstance()
        self.device = device
    
    def get_gpu_memory(self):
        """
        returns a tuple of [gpu_used_mem, gpu_total_mem]
        """
        gpu_query = self.nvsmi.DeviceQuery('memory.used, memory.total')
        #print(gpu_query)
        gpu_used_mem = int(gpu_query['gpu'][self.device.index]['fb_memory_usage']['used'])
        gpu_total_mem = int(gpu_query['gpu'][self.device.index]['fb_memory_usage']['total'])
        return gpu_used_mem, gpu_total_mem