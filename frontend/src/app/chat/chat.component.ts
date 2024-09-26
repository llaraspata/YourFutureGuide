import { ChangeDetectionStrategy, Component, ElementRef, ViewChild } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { Message } from './Message';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { LlmMessage } from './LlmMessage';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, MatCardModule, HttpClientModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css',
  changeDetection: ChangeDetectionStrategy.Default,
})


export class ChatComponent {
  @ViewChild("message", { static: false }) message?: ElementRef;
  selectedOption: number | null = null;

  chatMessagesUI: Message[] = [];
  chatMessagesLLM: LlmMessage[] = [];
  order = 0;

  rootYFG = "http://127.0.0.1:8000/"
  degreePredictionApi = "http://127.0.0.1:8000/predict/degree"
  careerPredictionApi = "http://127.0.0.1:8000/predict/career"

  isWriting = false;

  apiToCall = "";
  qst_count = 1;

  finalMessage: Message = {
    "display_order": 0,
    "type": "R",
    "content": "Com'è andata?",
    "options": []
  };


  constructor(private http: HttpClient) {
    let initialOptions = [
      {
        "id": 0,
        "icon": "📚",
        "content": "La laurea che meglio si allinea alle mie passioni",
        "message": "Vorrei scoprire la laurea che meglio si allinea alle mie passioni"
      },
      {
        "id": 1,
        "icon": "💼",
        "content": "Il percorso professionale perfetto per me",
        "message": "Vorrei scoprire il percorso professionale perfetto per me"
      } 
    ];

    this.chatMessagesUI = [
      {
        "display_order": 1,
        "type": "R", //received
        "content": "Cosa vorresti scoprire?",
        "options": initialOptions
      }
    ];

    let finalOptions = [
      {
        "id": 2,
        "icon": "✅",
        "content": "L'ho trovato interessante e piuttosto accurato!",
        "message": "Perfetto! Sono contento di averti aiutato!✨"
      },
      {
        "id": 3,
        "icon": "❌",
        "content": "Non mi ha convinto del tutto... Riproviamo, dai!",
        "message": ""
      },
    ];

    this.finalMessage.options = finalOptions;

    this.order = this.chatMessagesUI.length;
  }

  trackByMessageId(index: number, message: any): string {
    return message.id;
  }

  async startConversation(choosenOption: number) {
    console.log("QST count ->", this.qst_count);

    this.selectedOption = choosenOption;

    this.isWriting = true;

    if (choosenOption < 2) {
      this.apiToCall = "";

      if (choosenOption === 0) {
        this.apiToCall = this.degreePredictionApi;
      } 
      else if (choosenOption === 1) {
        this.apiToCall = this.careerPredictionApi;
      }

      this.addChoiseToChat(choosenOption);

      let newMsg = {
        "display_order": this.order++,
        "type": "R",
        "content": "",
        "options": []
      };

      this.postStartConversation().subscribe((response: any) => {
        this.chatMessagesLLM = response.chat_messages;

        newMsg.content = response.llm_output;

        this.chatMessagesUI.push(newMsg);
    
        this.qst_count++;
        this.isWriting = false;
      });
    }
    else if (choosenOption === 3) {
      window.location.reload();
    }
    else if (choosenOption === 2) {
      let newMsg = {
        "display_order": this.order++,
        "type": "R",
        "content": this.finalMessage.options[0].message,
        "options": []
      };
      this.isWriting = false;
      this.chatMessagesUI.push(newMsg);

    }
    
  }

  addChoiseToChat(choosenOption: number) {
    let newMsg = {
      "display_order": this.order++,
      "type": "S",
      "content": this.chatMessagesUI[0].options[choosenOption].message,
      "options": []
    };

    this.chatMessagesUI.push(newMsg);
  }

  postStartConversation() {
    const jsonPayload = {
      "usr_answer": "",
      "chat": [],
      "qst_count": 1
    };
    console.log(jsonPayload);
    
    return this.http.post(this.apiToCall, jsonPayload);
  }


  sendMessage() {
    if (!this.message?.nativeElement.value) {
      return;
    }

    let newMsg = {
      "display_order": this.order++,
      "type": "S",
      "content": this.message.nativeElement.value,
      "options": []
    };

    this.chatMessagesUI.push(newMsg);
    this.message.nativeElement.value = "";

    this.isWriting = true;

    this.postAnswer(newMsg.content).subscribe((response: any) => {
      this.chatMessagesLLM = response.chat_messages;

      let llmMsg = {
        "display_order": this.order++,
        "type": "R",
        "content": response.llm_output,
        "options": []
      };

      this.chatMessagesUI.push(llmMsg);
      this.isWriting = false;
      this.qst_count++;

      console.log(response.end_of_chat);

      if (response.end_of_chat) {
        this.chatMessagesUI.push(this.finalMessage);
      }
    });
  }

  postAnswer(usr_answer: string) {
    const jsonPayload = {
      "usr_answer": usr_answer,
      "chat": this.chatMessagesLLM,
      "qst_count": this.qst_count
    };

    return this.http.post(this.apiToCall, jsonPayload);
  }
  

}
