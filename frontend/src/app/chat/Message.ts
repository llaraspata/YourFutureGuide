import { Option } from "./Option";

export interface Message {
    display_order: number;
    type: string;
    content: string;
    options: Option[];
}